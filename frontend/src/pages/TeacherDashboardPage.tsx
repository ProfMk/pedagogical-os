import { useTeacherDashboard } from "../hooks/useTeacherDashboard";

const TeacherDashboardPage = (): JSX.Element => {
  const { data, loading, error } = useTeacherDashboard();

  if (loading) return <div>Loading dashboard...</div>;
  if (error) return <div>{error}</div>;
  if (!data) return <div>No data</div>;

  return (
    <div>
      <h1>Teacher Dashboard</h1>

      {data.groups.map((group) => (
        <div key={group.groupId}>
          <h2>{group.groupName}</h2>

          {group.students.map((student) => (
            <div key={student.studentId}>
              <h3>{student.studentName}</h3>

              {student.indicators.map((indicator) => (
                <div key={indicator.indicatorId}>
                  Stage {indicator.currentStage}/{indicator.totalStages} —
                  Consolidation: {indicator.consolidation}
                </div>
              ))}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default TeacherDashboardPage;
