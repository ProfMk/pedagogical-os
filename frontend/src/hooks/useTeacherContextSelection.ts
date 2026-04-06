import { useEffect, useMemo, useState } from 'react';

import { apiGet } from '../api/client';
import { getTeacherDashboard } from '../api/teacherDashboardApi';
import { getOpenPeriods } from '../modules/teacher-dashboard';

const INSTITUTION_ID = 'b1c31b99-f597-48fb-af2d-ad8fcbddc9bb';
const ACADEMIC_YEAR_ID = 'd3d61e45-e5a7-4f22-9860-811e73201326';
const TEACHER_ID = '11111111-1111-1111-1111-111111111111';

type TeacherGroup = {
  id: string;
  name: string;
  subject_id: string;
  subject_name: string;
};

type SubjectOption = {
  id: string;
  name: string;
};

export const useTeacherContextSelection = (): {
  groups: TeacherGroup[];
  subjects: SubjectOption[];
  openPeriods: ReturnType<typeof getOpenPeriods>;
  loading: boolean;
  error: string | null;
} => {
  const [groups, setGroups] = useState<TeacherGroup[]>([]);
  const [openPeriods, setOpenPeriods] = useState<ReturnType<typeof getOpenPeriods>>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadContext(): Promise<void> {
      try {
        setLoading(true);
        setError(null);
        const [groupsData, dashboardData] = await Promise.all([
          apiGet<TeacherGroup[]>(
            `/teacher/groups?teacher_id=${TEACHER_ID}&institution_id=${INSTITUTION_ID}&academic_year_id=${ACADEMIC_YEAR_ID}`
          ),
          getTeacherDashboard(INSTITUTION_ID, ACADEMIC_YEAR_ID, TEACHER_ID)
        ]);
        setGroups(groupsData);
        setOpenPeriods(getOpenPeriods(dashboardData.period));
      } catch {
        setError('Failed to load context');
      } finally {
        setLoading(false);
      }
    }

    void loadContext();
  }, []);

  const subjects = useMemo(() => {
    return Array.from(
      new Map(
        groups.map((group) => [
          group.subject_id,
          {
            id: group.subject_id,
            name: group.subject_name
          }
        ])
      ).values()
    );
  }, [groups]);

  return {
    groups,
    subjects,
    openPeriods,
    loading,
    error
  };
};