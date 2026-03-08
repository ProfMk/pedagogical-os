import { useParams } from 'react-router-dom';

import { Card } from '../components/ui/Card';

export const GroupPage = (): JSX.Element => {
  const { groupId } = useParams();

  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: 24 }}>
      <h1>Group Progress Page</h1>
      <Card>
        <p>Group progress placeholder.</p>
        <p>Selected group: {groupId}</p>
      </Card>
    </main>
  );
};
