import { memo, useMemo } from 'react';

import { Student } from '../../types/teacherDashboard';
import NucleusBlock from './NucleusBlock';

type Props = {
  student: Student;
  isOpen: boolean;
  onToggle: () => void;
};

const StudentRow = ({ student, isOpen, onToggle }: Props): JSX.Element => {
  const nucleusBlocks = useMemo(
    () =>
      student.nucleus.map((nucleus) => (
        <NucleusBlock key={nucleus.nucleusId} nucleus={nucleus} defaultOpen />
      )),
    [student.nucleus]
  );

  return (
    <li style={{ marginBottom: 16 }}>
      <div
        onClick={onToggle}
        style={{
          cursor: 'pointer',
          fontWeight: 700,
          userSelect: 'none',
          position: 'sticky',
          top: 0,
          background: '#fff',
          zIndex: 2,
          padding: '4px 0',
          borderBottom: '1px solid #eee'
        }}
      >
        {isOpen ? '▼' : '▶'} {student.studentName}
      </div>

      <div
        style={{
          maxHeight: isOpen ? 4000 : 0,
          overflow: 'hidden',
          transition: 'max-height 0.25s ease'
        }}
      >
        {isOpen && <div style={{ marginTop: 8 }}>{nucleusBlocks}</div>}
      </div>
    </li>
  );
};

export default memo(StudentRow);
