import { Indicator } from '../../types/teacherDashboard';
import Tooltip from '../ui/Tooltip';

type IndicatorNodeProps = {
  indicator: Indicator;
};

type IndicatorWithStages = Indicator & {
  stageColors?: string[];
};

const getBlock = (color?: string): string => {
  switch ((color || '').toLowerCase()) {
    case 'green':
      return '🟩';
    case 'yellow':
      return '🟨';
    case 'red':
      return '🟥';
    default:
      return '⬜';
  }
};

const getLevelColor = (level: number | null): string => {
  if (level === null) return '⬜';
  if (level >= 4) return '🟩';
  if (level >= 2.5) return '🟨';
  return '🟥';
};

const IndicatorNode = ({ indicator }: IndicatorNodeProps): JSX.Element => {
  const enriched = indicator as IndicatorWithStages;

  const hasStageColors =
    Array.isArray(enriched.stageColors) &&
    enriched.stageColors.length === indicator.totalStages;

  const stageBlocks = hasStageColors
    ? enriched.stageColors!.map((color, index) => (
        <span key={`${indicator.indicatorId}-${index}`}>
          {getBlock(color)}
        </span>
      ))
    : Array.from({ length: indicator.totalStages }, (_, index) => {
        const filled = index < indicator.currentStage;
        return (
          <span key={`${indicator.indicatorId}-${index}`}>
            {filled ? getLevelColor(indicator.normalizedLevel) : '⬜'}
          </span>
        );
      });

  const hasCurrentStageIssue = indicator.consolidation === null;

  return (
    <li style={{ marginBottom: 8 }}>
      <Tooltip
        content={
          <>
            <div>ID: {indicator.indicatorId}</div>
            <div>
              Stage: {indicator.currentStage}/{indicator.totalStages}
            </div>
            <div>Level: {indicator.normalizedLevel ?? 'N/A'}</div>
          </>
        }
      >
        <div>
          <div style={{ fontSize: 12, opacity: 0.7 }}>
            {indicator.indicatorId}
          </div>

          <div
            aria-label="stage-blocks"
            style={{
              fontSize: 18,
              display: 'flex',
              gap: 4,
              margin: '4px 0'
            }}
          >
            {stageBlocks}
          </div>
        </div>
      </Tooltip>

      <div>
        Stage: {indicator.currentStage} / {indicator.totalStages}
      </div>

      {indicator.normalizedLevel !== null && (
        <div>Level: {indicator.normalizedLevel}</div>
      )}

      {hasCurrentStageIssue && (
        <div style={{ color: '#e67e22' }}>
          ⚠️ Current stage not consolidated
        </div>
      )}

      {!hasStageColors && (
        <div style={{ fontSize: 11, opacity: 0.5 }}>
          Visual approximation (no stage-level consolidation data)
        </div>
      )}
    </li>
  );
};

export default IndicatorNode;