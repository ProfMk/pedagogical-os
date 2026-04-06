type Props = {
  indicators: {
    stage_average: number;
    total_stages: number;
  }[];
};

const getColor = (ratio: number): string => {
  if (ratio >= 0.8) return '#2ecc71';
  if (ratio >= 0.5) return '#f1c40f';
  return '#e74c3c';
};

const GroupHeatmap = ({ indicators }: Props): JSX.Element => {
  return (
    <div style={{ display: 'flex', gap: 4 }}>
      {indicators.map((ind, i) => {
        const ratio = ind.stage_average / ind.total_stages;

        return (
          <div
            key={i}
            style={{
              width: 20,
              height: 20,
              background: getColor(ratio),
              borderRadius: 3
            }}
          />
        );
      })}
    </div>
  );
};

export default GroupHeatmap;