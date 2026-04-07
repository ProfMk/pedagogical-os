import { useState } from 'react';

import { Student } from '../../types/teacherDashboard';
import NucleusBlock from './NucleusBlock';

type StudentNodeProps = {
  student: Student;
};

const StudentNode = ({ student }: StudentNodeProps): JSX.Element => {
  const [isExpanded, setIsExpanded] = useState<boolean>(false);

  return (
    <li>
      <button type="button" onClick={() => setIsExpanded((value) => !value)}>
        {isExpanded ? '−' : '+'} {student.studentName}
      </button>

      {isExpanded && (
        <div style={{ marginTop: 8 }}>
          {student.nucleus.map((nucleus) => (
            <NucleusBlock key={nucleus.nucleusId} nucleus={nucleus} defaultOpen />
          ))}
        </div>
      )}
    </li>
  );
};

export default StudentNode;
