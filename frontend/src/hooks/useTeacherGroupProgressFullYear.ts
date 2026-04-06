import { useEffect, useState } from 'react';
import { apiGet } from '../api/client';
import { useTeacherStore } from '../state/teacherStore';

const INSTITUTION_ID = 'b1c31b99-f597-48fb-af2d-ad8fcbddc9bb';
const ACADEMIC_YEAR_ID = 'd3d61e45-e5a7-4f22-9860-811e73201326';
const TEACHER_ID = '11111111-1111-1111-1111-111111111111';

export type GroupProgressTree = {
  group_id: string;
  group_name: string;
  nuclei: {
    nucleus_id: string;
    name: string;
    competencies: {
      competency_id: string;
      description: string;
      indicators: {
        indicator_id: string;
        description: string;
        stage_average: number;
        consolidation_average: number;
        total_stages: number;
      }[];
    }[];
  }[];
};

export const useTeacherGroupProgressFullYear = () => {
  const { subjectId, groupId } = useTeacherStore();

  const [tree, setTree] = useState<GroupProgressTree | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load() {
      if (!subjectId || !groupId) {
        setTree(null);
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
        setError('Failed to load group progress');
      } finally {
        setLoading(false);
      }
    }

    void load();
  }, [subjectId, groupId]);

  return { tree, loading, error };
};