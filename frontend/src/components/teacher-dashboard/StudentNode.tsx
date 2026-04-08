import { useMemo, useState } from 'react';

import { Indicator, Student } from '../../types/teacherDashboard';
import IndicatorNode from './IndicatorNode';

type StudentNodeProps = {
  student: Student;
};

const StudentNode = ({ student }: StudentNodeProps): JSX.Element => {
  const [isExpanded, setIsExpanded] = useState<boolean>(false);
  const groupedIndicators = useMemo(() => {
    type IndicatorWithGrouping = Indicator & {
      nucleus_id?: string | null;
      nucleus_name?: string | null;
      competence_id?: string | null;
      competence_name?: string | null;
    };

    const grouped = new Map<
      string,
      {
        nucleusName: string;
        competences: Map<
          string,
          {
            competenceName: string;
            indicators: Indicator[];
          }
        >;
      }
    >();

    student.indicators.forEach((rawIndicator) => {
      const indicator = rawIndicator as IndicatorWithGrouping;
      const nucleusId = indicator.nucleus_id;
      const competenceId = indicator.competence_id;

      if (nucleusId === null || nucleusId === undefined) return;
      if (competenceId === null || competenceId === undefined) return;

      if (!grouped.has(nucleusId)) {
        grouped.set(nucleusId, {
          nucleusName: indicator.nucleus_name ?? nucleusId,
          competences: new Map()
        });
      }

      const nucleus = grouped.get(nucleusId)!;

      if (!nucleus.competences.has(competenceId)) {
        nucleus.competences.set(competenceId, {
          competenceName: indicator.competence_name ?? competenceId,
          indicators: []
        });
      }

      nucleus.competences.get(competenceId)!.indicators.push(rawIndicator);
    });

    return grouped;
  }, [student.indicators]);

  return (
    <li>
      <button type="button" onClick={() => setIsExpanded((value) => !value)}>
        {isExpanded ? '−' : '+'} {student.studentName}
      </button>

      {isExpanded && (
        <ul>
          {groupedIndicators.size === 0 && <li>No indicators available</li>}

          {Array.from(groupedIndicators.entries()).map(
            ([nucleusId, nucleus]) => (
              <li key={nucleusId}>
                <div style={{ fontWeight: 700, marginTop: 8 }}>
                  {nucleus.nucleusName}
                </div>
                <ul>
                  {Array.from(nucleus.competences.entries()).map(
                    ([competenceId, competence]) => (
                      <li key={competenceId}>
                        <div style={{ fontWeight: 600, marginTop: 6 }}>
                          {competence.competenceName}
                        </div>
                        <ul>
                          {competence.indicators.map((indicator) => (
                            <IndicatorNode
                              key={indicator.indicatorId}
                              indicator={indicator}
                            />
                          ))}
                        </ul>
                      </li>
                    )
                  )}
                </ul>
              </li>
            )
          )}
        </ul>
      )}
    </li>
  );
};

export default StudentNode;
