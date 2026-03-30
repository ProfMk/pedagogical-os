import { Indicator } from '../../types/teacherDashboard';

type IndicatorNodeProps = {
  indicator: Indicator;
};

const IndicatorNode = ({ indicator }: IndicatorNodeProps): JSX.Element => {
  return (
    <li>
      <div>{indicator.indicatorId}</div>
      <div>
        Stage {indicator.currentStage} / {indicator.totalStages}
      </div>
      {indicator.consolidation !== null && <div>{indicator.consolidation}</div>}
      {indicator.normalizedLevel !== null && <div>{indicator.normalizedLevel}</div>}
    </li>
  );
};

export default IndicatorNode;
