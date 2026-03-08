import { useParams } from 'react-router-dom';

import { StudentTable } from '../components/tables/StudentTable';
import { Card } from '../components/ui/Card';
import { useStudents } from '../hooks/useStudents';

export const StudentPage = (): JSX.Element => {
  const { studentId } = useParams();
  const { data, loading, error } = useStudents();

  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: 24 }}>
      <h1>Student Progress Page</h1>
      <Card>
        <p>Student progress placeholder.</p>
        <p>Route student id: {studentId}</p>
        {loading && <p>Loading students...</p>}
        {error && <p>{error}</p>}
        {data && <StudentTable students={data.students} />}
      </Card>
    </main>
  );
};
