import { useMemo } from 'react';
import GroupNode from '../components/teacher-dashboard/GroupNode';
import { useTeacherContextSelection } from '../hooks/useTeacherContextSelection';
import { useTeacherDashboard } from '../hooks/useTeacherDashboard';
import { useTeacherStore } from '../state/teacherStore';

const TeacherDashboardPage = (): JSX.Element => {
  const { data, loading, error } = useTeacherDashboard();
  const { groups, subjects, openPeriods, loading: contextLoading, error: contextError } = useTeacherContextSelection();
  const { subjectId, groupId, academicPeriodId, setSubject, setGroup, setPeriod } = useTeacherStore();

  const availableGroups = useMemo(
    () => groups.filter((group) => group.subject_id === subjectId),
    [groups, subjectId]
  );
  const canLoadDashboard = Boolean(subjectId && groupId && academicPeriodId);

  if (contextLoading || loading) {
    return <div>Loading dashboard...</div>;
  }

  if (contextError || error) {
    return <div>{contextError || error}</div>;
  }

  return (
    <div>
      <div style={{ marginBottom: 16 }}>
        <a href="/dashboard">← Back to Dashboard</a>
      </div>
      <h1>Teacher Dashboard</h1>

      <section style={{ display: 'grid', gap: 12, marginBottom: 16 }}>
        <div>
          <h2>Subject</h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))', gap: 8 }}>
            {subjects.map((subject) => (
              <button
                key={subject.id}
                type="button"
                onClick={() => setSubject(subject.id)}
                style={{ fontWeight: subjectId === subject.id ? 700 : 400 }}
              >
                {subject.name}
              </button>
            ))}
          </div>
        </div>

        {subjectId && (
          <div>
            <h2>Group</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: 8 }}>
              {availableGroups.map((group) => (
                <button
                  key={group.id}
                  type="button"
                  onClick={() => setGroup(group.id)}
                  style={{ fontWeight: groupId === group.id ? 700 : 400 }}
                >
                  {group.name}
                </button>
              ))}
            </div>
          </div>
        )}

        {groupId && (
          <div>
            <h2>Period</h2>
            {openPeriods.length === 0 && <p>No open periods available.</p>}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: 8 }}>
              {openPeriods.map((period) => (
                <button
                  key={period.id}
                  type="button"
                  onClick={() => setPeriod(period.id)}
                  style={{ fontWeight: academicPeriodId === period.id ? 700 : 400 }}
                >
                  {period.name}
                </button>
              ))}
            </div>
          </div>
        )}
      </section>

      {!canLoadDashboard && <p>Select subject, group, and period to continue.</p>}

      {canLoadDashboard && data && data.groups.length > 0 && (
        <ul>
          {data.groups.map((group) => (
            <GroupNode key={group.groupId} group={group} />
          ))}
        </ul>
      )}
    </div>
  );
};

export default TeacherDashboardPage;