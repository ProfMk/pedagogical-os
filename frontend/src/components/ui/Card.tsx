import { PropsWithChildren } from 'react';

export const Card = ({ children }: PropsWithChildren): JSX.Element => {
  return (
    <section style={{ border: '1px solid #d0d7de', borderRadius: 8, padding: 16, marginBottom: 16 }}>
      {children}
    </section>
  );
};
