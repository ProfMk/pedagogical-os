import { useMemo } from 'react';

import { useTeacherContextSelection } from '../hooks/useTeacherContextSelection';
import { useTeacherGroupProgress } from '../hooks/useTeacherGroupProgress';
import { useTeacherStore } from '../state/teacherStore';

const TeacherGroupProgressPage = (): JSX.Element => {
  const { groups, subjects: subjectOptions, openPeriods, loading: contextLoading, error: contextError } =
    useTeacherContextSelection();
  const { tree, loading, error } = useTeacherGroupProgress();
  const { subjectId, groupId, academicPeriodId, setSubject, setGroup, setPeriod } = useTeacherStore();

  const groupOptions = useMemo(() => {
    return groups.filter((group) => group.subject_id === subjectId);
  }, [groups, subjectId]);

  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: 24 }}>
      <div style={{ marginBottom: 16 }}>
        <a href="/dashboard">← Back to Dashboard</a>
      </div>
      <h1>Teacher Group Progress</h1>
      {contextLoading && <p>Loading context...</p>}
      {contextError && <p>{contextError}</p>}

      <div>
        <h2>Subject</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))', gap: 8 }}>
          {subjectOptions.map((subject) => (
            <button
              key={subject.id}
              type="button"
              onClick={() => setSubject(subject.id)}
              style={{ fontWeight: subject.id === subjectId ? 700 : 400 }}
            >
              {subject.name}
            </button>
          ))}
        </div>
      </div>

      {subjectId && (
        <div style={{ marginTop: 12 }}>
          <h2>Group</h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: 8 }}>
            {groupOptions.map((group) => (
              <button
                key={group.id}
                type="button"
                onClick={() => setGroup(group.id)}
                style={{ fontWeight: group.id === groupId ? 700 : 400 }}
              >
                {group.name}
              </button>
            ))}
          </div>
        </div>
      )}

      {groupId && (
        <div style={{ marginTop: 12 }}>
          <h2>Period</h2>
          {openPeriods.length === 0 && <p>No open periods available.</p>}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: 8 }}>
            {openPeriods.map((period) => (
              <button
                key={period.id}
                type="button"
                onClick={() => setPeriod(period.id)}
                style={{ fontWeight: period.id === academicPeriodId ? 700 : 400 }}
              >
                {period.name}
              </button>
            ))}
          </div>
        </div>
      )}

      {loading && <p>Loading group progress tree...</p>}
      {error && <p>{error}</p>}
      {!subjectId || !groupId || !academicPeriodId ? <p>Select subject, group, and period to continue.</p> : null}

      {subjectId && groupId && academicPeriodId && tree && (
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