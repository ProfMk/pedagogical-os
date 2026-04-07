import { memo, useMemo, useState } from 'react';

import { Nucleus } from '../../types/teacherDashboard';
import CompetenceBlock from './CompetenceBlock';

type Props = {
  nucleus: Nucleus;
  defaultOpen?: boolean;
};

const NucleusBlock = ({ nucleus, defaultOpen = true }: Props): JSX.Element => {
  const [isOpen, setIsOpen] = useState<boolean>(defaultOpen);

  const competenceBlocks = useMemo(
    () =>
      nucleus.competences.map((competence) => (
        <CompetenceBlock key={competence.competenceId} competence={competence} />
      )),
    [nucleus.competences]
  );

  const avgLabel =
    nucleus.averageNormalizedLevel === null
      ? 'N/A'
      : nucleus.averageNormalizedLevel.toFixed(2);

  return (
    <div
      style={{
        marginLeft: 0,
        paddingBottom: 12,
        borderBottom: '1px solid #eee',
        marginBottom: 12,
      }}
    >
      <button
        type="button"
        onClick={() => setIsOpen((value) => !value)}
        style={{
          cursor: 'pointer',
          userSelect: 'none',
          border: 'none',
          background: 'transparent',
          padding: 0,
          marginBottom: 4,
          fontWeight: 700,
          textTransform: 'uppercase',
        }}
      >
        {isOpen ? '▼' : '▶'} {nucleus.nucleusName}
      </button>

      <div style={{ fontSize: 12, opacity: 0.8, marginBottom: 8 }}>
        Avg level: {avgLabel} · Competences: {nucleus.competenceCount}
      </div>

      <div
        style={{
          maxHeight: isOpen ? 3000 : 0,
          overflow: 'hidden',
          transition: 'max-height 0.25s ease',
        }}
      >
        {isOpen && <div>{competenceBlocks}</div>}
      </div>
    </div>
  );
};

export default memo(NucleusBlock);
