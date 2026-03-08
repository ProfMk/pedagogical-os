type Student = {
  id: string;
  name: string;
};

type StudentTableProps = {
  students: Student[];
};

export const StudentTable = ({ students }: StudentTableProps): JSX.Element => {
  return (
    <table style={{ width: '100%', borderCollapse: 'collapse' }}>
      <thead>
        <tr>
          <th style={{ borderBottom: '1px solid #d0d7de', textAlign: 'left' }}>ID</th>
          <th style={{ borderBottom: '1px solid #d0d7de', textAlign: 'left' }}>Name</th>
        </tr>
      </thead>
      <tbody>
        {students.map((student) => (
          <tr key={student.id}>
            <td style={{ paddingTop: 8 }}>{student.id}</td>
            <td style={{ paddingTop: 8 }}>{student.name}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
