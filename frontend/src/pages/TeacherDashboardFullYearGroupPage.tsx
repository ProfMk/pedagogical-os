import { useMemo } from 'react';
import { useTeacherGroupProgressFullYear } from '../hooks/useTeacherGroupProgressFullYear';
import { useTeacherContextSelection } from '../hooks/useTeacherContextSelection';
import { useTeacherStore } from '../state/teacherStore';

const TeacherDashboardFullYearGroupPage = (): JSX.Element => {
  const { tree, loading, error } = useTeacherGroupProgressFullYear();
  const { groups, subjects } = useTeacherContextSelection();
  const { subjectId, groupId, setSubject, setGroup } = useTeacherStore();

  const availableGroups = useMemo(
    () => groups.filter((g) => g.subject_id === subjectId),
    [groups, subjectId]
  );

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <a href="/teacher/dashboard-full-year">← Back</a>

      <h1>Full Year — Group View</h1>

      {/* SUBJECT */}
      <section>
        <h2>Subject</h2>
        <div style={{ display: 'grid', gap: 8 }}>
          {subjects.map((s) => (
            <button
              key={s.id}
              type="button"
              onClick={() => setSubject(s.id)}
              style={{ fontWeight: subjectId === s.id ? 700 : 400 }}
            >
              {s.name}
            </button>
          ))}
        </div>
      </section>

      {/* GROUP */}
      {subjectId && (
        <section style={{ marginTop: 16 }}>
          <h2>Group</h2>
          <div style={{ display: 'grid', gap: 8 }}>
            {availableGroups.map((g) => (
              <button
                key={g.id}
                type="button"
                onClick={() => setGroup(g.id)}
                style={{ fontWeight: groupId === g.id ? 700 : 400 }}
              >
                {g.name}
              </button>
            ))}
          </div>
        </section>
      )}

      {/* AGGREGATED TREE */}
      {subjectId && groupId && tree && (
        <section style={{ marginTop: 24 }}>
          <h2>Group Progress</h2>

          <ul>
            {tree.nuclei.map((nucleus) => (
              <li key={nucleus.nucleus_id}>
                <strong>Nucleus:</strong> {nucleus.name}

                <ul>
                  {nucleus.competencies.map((comp) => (
                    <li key={comp.competency_id}>
                      <strong>Competency:</strong> {comp.description}

                      <ul>
                        {comp.indicators.map((ind) => (
                          <li key={ind.indicator_id}>
                            <div>
                              {ind.description}
                            </div>

                            <div>
                              Stage Avg: {ind.stage_average} / {ind.total_stages}
                            </div>

                            <div>
                              Consolidation Avg: {ind.consolidation_average}
                            </div>
                          </li>
                        ))}
                      </ul>
                    </li>
                  ))}
                </ul>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
};

export default TeacherDashboardFullYearGroupPage;