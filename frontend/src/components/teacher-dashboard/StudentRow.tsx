import { useMemo } from 'react';

import IndicatorNode from './IndicatorNode';
import { Indicator, Student } from '../../types/teacherDashboard';

type Props = {
  student: Student;
  isOpen: boolean;
  onToggle: () => void;
};

const StudentRow = ({ student, isOpen, onToggle }: Props): JSX.Element => {
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
      </div>
    </li>
  );
};

export default StudentRow;
