import GroupNode from '../components/teacher-dashboard/GroupNode';
import { useTeacherDashboard } from '../hooks/useTeacherDashboard';

const TeacherDashboardPage = (): JSX.Element => {
  const { data, loading, error } = useTeacherDashboard();

  if (loading) {
    return <div>Loading dashboard...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (!data || data.groups.length === 0) {
    return <div>No groups available.</div>;
  }

  return (
    <div>
      <h1>Teacher Dashboard</h1>
      <ul>
        {data.groups.map((group) => (
          <GroupNode key={group.groupId} group={group} />
        ))}
      </ul>
    </div>
  );
};

export default TeacherDashboardPage;
