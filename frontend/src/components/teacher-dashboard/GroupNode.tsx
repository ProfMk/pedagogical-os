import { useState } from 'react';

import { Group } from '../../types/teacherDashboard';
import StudentNode from './StudentNode';

type GroupNodeProps = {
  group: Group;
};

const GroupNode = ({ group }: GroupNodeProps): JSX.Element => {
  const [isExpanded, setIsExpanded] = useState<boolean>(false);

  return (
    <li>
      <button type="button" onClick={() => setIsExpanded((value) => !value)}>
        {isExpanded ? '−' : '+'} {group.groupName}
      </button>

      {isExpanded && (
        <ul>
          {group.students.map((student) => (
            <StudentNode key={student.studentId} student={student} />
          ))}
        </ul>
      )}
    </li>
  );
};

export default GroupNode;
