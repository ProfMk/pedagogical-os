import { useNavigate } from 'react-router-dom';

const TeacherDashboardFullYearPage = (): JSX.Element => {
  const navigate = useNavigate();

  return (
    <div>
      <a href="/dashboard">← Back</a>
      <h1>Full Year Dashboard</h1>

      <div>
        <button onClick={() => navigate('/teacher/dashboard-full-year/group')}>
          Group View
        </button>

        <button onClick={() => navigate('/teacher/dashboard-full-year/student')}>
          Student View
        </button>
      </div>
    </div>
  );
};

export default TeacherDashboardFullYearPage;