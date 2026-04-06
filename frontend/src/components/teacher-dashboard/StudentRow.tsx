import IndicatorNode from './IndicatorNode';
import { Student } from '../../types/teacherDashboard';

type Props = {
  student: Student;
  isOpen: boolean;
  onToggle: () => void;
};

const StudentRow = ({ student, isOpen, onToggle }: Props): JSX.Element => {
  return (
    <li style={{ marginBottom: 16 }}>
      {/* STICKY HEADER */}
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

      {/* EXPANSION FIXED */}
      <div
        style={{
          maxHeight: isOpen ? 1000 : 0,
          overflow: 'hidden',
          transition: 'max-height 0.25s ease'
        }}
      >
        {/* LAZY RENDER REAL */}
        {isOpen && (
          <ul style={{ marginTop: 8 }}>
            {student.indicators.map((indicator) => (
              <IndicatorNode
                key={indicator.indicatorId}
                indicator={indicator}
              />
            ))}
          </ul>
        )}
      </div>
    </li>
  );
};

export default StudentRow;