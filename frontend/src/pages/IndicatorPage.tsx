import { useParams } from 'react-router-dom';

import { Card } from '../components/ui/Card';
import { ProgressBar } from '../components/ui/ProgressBar';
import { useIndicators } from '../hooks/useIndicators';

export const IndicatorPage = (): JSX.Element => {
  const { indicatorId } = useParams();
  const { data, loading, error } = useIndicators();

  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: 24 }}>
      <h1>Indicator View Page</h1>
      <Card>
        <p>Indicator page placeholder.</p>
        <p>Route indicator id: {indicatorId}</p>
        {loading && <p>Loading indicators...</p>}
        {error && <p>{error}</p>}
        {data && (
          <ul>
            {data.indicators.map((indicator) => (
              <li key={indicator.id}>{indicator.label}</li>
            ))}
          </ul>
        )}
        <ProgressBar value={35} />
      </Card>
    </main>
  );
};
