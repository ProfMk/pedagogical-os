import { useEffect, useState } from 'react';

import { apiGet } from '../api/client';
import { useTeacherStore } from '../state/teacherStore';

const INSTITUTION_ID = 'b1c31b99-f597-48fb-af2d-ad8fcbddc9bb';
const ACADEMIC_YEAR_ID = 'd3d61e45-e5a7-4f22-9860-811e73201326';
const TEACHER_ID = '11111111-1111-1111-1111-111111111111';

type IndicatorProgress = {
  indicator_id: string;
  description: string;
  stage_average: number;
  consolidation_average: number;
  total_stages: number;
};

type CompetencyNode = {
  competency_id: string;
  description: string;
  indicators: IndicatorProgress[];
};

type NucleusNode = {
  nucleus_id: string;
  name: string;
  competencies: CompetencyNode[];
};

export type GroupProgressTree = {
  group_id: string;
  group_name: string;
  nuclei: NucleusNode[];
};

export const useTeacherGroupProgress = (): {
  tree: GroupProgressTree | null;
  loading: boolean;
  error: string | null;
} => {
  const { subjectId, groupId, academicPeriodId } = useTeacherStore();
  const [tree, setTree] = useState<GroupProgressTree | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadTree(): Promise<void> {
      if (!subjectId || !groupId || !academicPeriodId) {
        setTree(null);
        setLoading(false);
        setError(null);
        return;
      }

      setLoading(true);
      setError(null);

      try {
        const data = await apiGet<GroupProgressTree>(
          `/teacher/group-indicator-tree?institution_id=${INSTITUTION_ID}&academic_year_id=${ACADEMIC_YEAR_ID}&teacher_id=${TEACHER_ID}&subject_id=${subjectId}&group_id=${groupId}`
        );
        setTree(data);
      } catch {
        setError('Failed to load group progress tree');
      } finally {
        setLoading(false);
      }
    }

    void loadTree();
  }, [subjectId, groupId, academicPeriodId]);

  return {
    tree,
    loading,
    error
  };
};