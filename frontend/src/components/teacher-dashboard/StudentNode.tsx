import { useState } from 'react';

import { Student } from '../../types/teacherDashboard';
import IndicatorNode from './IndicatorNode';

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
        <ul>
          {student.indicators.map((indicator) => (
            <IndicatorNode key={indicator.indicatorId} indicator={indicator} />
          ))}
        </ul>
      )}
    </li>
  );
};

export default StudentNode;
