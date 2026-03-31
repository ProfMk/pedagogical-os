import { useEffect, useMemo, useState } from 'react';

import { apiGet } from '../api/client';

const INSTITUTION_ID = 'b1c31b99-f597-48fb-af2d-ad8fcbddc9bb';
const ACADEMIC_YEAR_ID = 'd3d61e45-e5a7-4f22-9860-811e73201326';
const TEACHER_ID = '11111111-1111-1111-1111-111111111111';

type TeacherGroup = {
  id: string;
  name: string;
  subject_id: string;
  subject_name: string; // ✅ FIX
  academic_year_id: string;
};

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

type GroupProgressTree = {
  group_id: string;
  group_name: string;
  nuclei: NucleusNode[];
};

const TeacherGroupProgressPage = (): JSX.Element => {
  const [groups, setGroups] = useState<TeacherGroup[]>([]);
  const [selectedSubjectId, setSelectedSubjectId] = useState<string>('');
  const [selectedGroupId, setSelectedGroupId] = useState<string>('');
  const [tree, setTree] = useState<GroupProgressTree | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadGroups(): Promise<void> {
      try {
        const data = await apiGet<TeacherGroup[]>(
          `/teacher/groups?teacher_id=${TEACHER_ID}&institution_id=${INSTITUTION_ID}&academic_year_id=${ACADEMIC_YEAR_ID}`
        );
        setGroups(data);
      } catch {
        setError('Failed to load groups');
      }
    }

    void loadGroups();
  }, []);

  // ✅ FIX COMPLETO
  const subjectOptions = useMemo(() => {
    return Array.from(
      new Map(
        groups.map((group) => [
          group.subject_id,
          {
            id: group.subject_id,
            name: group.subject_name,
          },
        ])
      ).values()
    );
  }, [groups]);

  const groupOptions = useMemo(() => {
    return groups.filter((group) => group.subject_id === selectedSubjectId);
  }, [groups, selectedSubjectId]);

  useEffect(() => {
    setSelectedGroupId('');
    setTree(null);
  }, [selectedSubjectId]);

  useEffect(() => {
    async function loadTree(): Promise<void> {
      if (!selectedSubjectId || !selectedGroupId) {
        return;
      }

      setLoading(true);
      setError(null);

      try {
        const data = await apiGet<GroupProgressTree>(
          `/teacher/group-indicator-tree?institution_id=${INSTITUTION_ID}&academic_year_id=${ACADEMIC_YEAR_ID}&teacher_id=${TEACHER_ID}&subject_id=${selectedSubjectId}&group_id=${selectedGroupId}`
        );
        setTree(data);
      } catch {
        setError('Failed to load group progress tree');
      } finally {
        setLoading(false);
      }
    }

    void loadTree();
  }, [selectedSubjectId, selectedGroupId]);

  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: 24 }}>
      <div style={{ marginBottom: 16 }}>
        <a href="/dashboard">← Back to Dashboard</a>
      </div>
      <h1>Teacher Group Progress</h1>

      <div>
        <label htmlFor="subject-select">Subject: </label>
        <select
          id="subject-select"
          value={selectedSubjectId}
          onChange={(event) => setSelectedSubjectId(event.target.value)}
        >
          <option value="">Select a subject</option>
          {subjectOptions.map((subject) => (
            <option key={subject.id} value={subject.id}>
              {subject.name}
            </option>
          ))}
        </select>
      </div>

      <div style={{ marginTop: 12 }}>
        <label htmlFor="group-select">Group: </label>
        <select
          id="group-select"
          value={selectedGroupId}
          onChange={(event) => setSelectedGroupId(event.target.value)}
          disabled={!selectedSubjectId}
        >
          <option value="">Select a group</option>
          {groupOptions.map((group) => (
            <option key={group.id} value={group.id}>
              {group.name}
            </option>
          ))}
        </select>
      </div>

      {loading && <p>Loading group progress tree...</p>}
      {error && <p>{error}</p>}

      {tree && (
        <div style={{ marginTop: 24 }}>
          <h2>
            Group: {tree.group_name || tree.group_id}
          </h2>
          <ul>
            {tree.nuclei.map((nucleus) => (
              <li key={nucleus.nucleus_id}>
                <strong>Nucleus:</strong> {nucleus.name}
                <ul>
                  {nucleus.competencies.map((competency) => (
                    <li key={competency.competency_id}>
                      <strong>Competency:</strong> {competency.description}
                      <ul>
                        {competency.indicators.map((indicator) => (
                          <li key={indicator.indicator_id}>
                            {indicator.description} — Stage Avg: {indicator.stage_average} / {indicator.total_stages} — Consolidation Avg: {indicator.consolidation_average}
                          </li>
                        ))}
                      </ul>
                    </li>
                  ))}
                </ul>
              </li>
            ))}
          </ul>
        </div>
      )}
    </main>
  );
};

export default TeacherGroupProgressPage;