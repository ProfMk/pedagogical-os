import { useMemo, useState } from 'react';
import { useTeacherDashboardFullYear } from '../hooks/useTeacherDashboardFullYear';
import { useTeacherContextSelection } from '../hooks/useTeacherContextSelection';
import { useTeacherStore } from '../state/teacherStore';
import StudentRow from '../components/teacher-dashboard/StudentRow';

const TeacherDashboardFullYearStudentPage = (): JSX.Element => {
  const { data, loading, error } = useTeacherDashboardFullYear();
  const { groups, subjects } = useTeacherContextSelection();
  const { subjectId, groupId, setSubject, setGroup } = useTeacherStore();

  const [openStudents, setOpenStudents] = useState<Record<string, boolean>>({});

  const toggleStudent = (id: string) => {
    setOpenStudents((prev) => ({
      ...prev,
      [id]: !prev[id],
    }));
  };

  const availableGroups = useMemo(
    () => groups.filter((g) => g.subject_id === subjectId),
    [groups, subjectId]
  );

  const selectedGroup = useMemo(
    () => data?.groups.find((g) => g.groupId === groupId),
    [data, groupId]
  );

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div style={{ paddingBottom: 40 }}>
      <a href="/teacher/dashboard-full-year">← Back</a>

      <h1>Full Year — Student View</h1>

      {/* SUBJECT */}
      <h2>Subject</h2>
      <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
        {subjects.map((s) => (
          <button
            key={s.id}
            onClick={() => setSubject(s.id)}
            style={{
              fontWeight: subjectId === s.id ? 700 : 400
            }}
          >
            {s.name}
          </button>
        ))}
      </div>

      {/* GROUP */}
      {subjectId && (
        <>
          <h2>Group</h2>
          <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
            {availableGroups.map((g) => (
              <button
                key={g.id}
                onClick={() => setGroup(g.id)}
                style={{
                  fontWeight: groupId === g.id ? 700 : 400
                }}
              >
                {g.name}
              </button>
            ))}
          </div>
        </>
      )}

      {/* STUDENTS */}
      {groupId && selectedGroup && (
        <ul style={{ marginTop: 20 }}>
          {selectedGroup.students.map((student) => (
            <StudentRow
              key={student.studentId}
              student={student}
              isOpen={!!openStudents[student.studentId]}
              onToggle={() => toggleStudent(student.studentId)}
            />
          ))}
        </ul>
      )}
    </div>
  );
};

export default TeacherDashboardFullYearStudentPage;