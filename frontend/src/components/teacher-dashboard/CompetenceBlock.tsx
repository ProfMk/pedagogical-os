import { memo, useMemo, useState } from 'react';

import { Competence } from '../../types/teacherDashboard';
import IndicatorNode from './IndicatorNode';

type Props = {
  competence: Competence;
};

const CompetenceBlock = ({ competence }: Props): JSX.Element => {
  const [isOpen, setIsOpen] = useState<boolean>(false);

  const indicatorNodes = useMemo(
    () =>
      competence.indicators.map((indicator) => (
        <IndicatorNode key={indicator.indicatorId} indicator={indicator} />
      )),
    [competence.indicators]
  );

  const avgLabel =
    competence.averageNormalizedLevel === null
      ? 'N/A'
      : competence.averageNormalizedLevel.toFixed(2);

  return (
    <div style={{ marginLeft: 16, marginBottom: 8 }}>
      <button
        type="button"
        onClick={() => setIsOpen((value) => !value)}
        style={{
          cursor: 'pointer',
          border: 'none',
          background: 'transparent',
          padding: 0,
          fontWeight: 500,
        }}
      >
        {isOpen ? '▼' : '▶'} {competence.competenceName}
      </button>

      <div style={{ fontSize: 12, opacity: 0.75, marginTop: 2 }}>
        Avg level: {avgLabel} · Indicators: {competence.indicatorCount}
      </div>

      <div
        style={{
          maxHeight: isOpen ? 2000 : 0,
          overflow: 'hidden',
          transition: 'max-height 0.25s ease',
          marginLeft: 16,
        }}
      >
        {isOpen && <ul style={{ marginTop: 8 }}>{indicatorNodes}</ul>}
      </div>
    </div>
  );
};

export default memo(CompetenceBlock);
