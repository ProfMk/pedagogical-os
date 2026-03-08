type ProgressBarProps = {
  value: number;
};

export const ProgressBar = ({ value }: ProgressBarProps): JSX.Element => {
  const boundedValue = Math.max(0, Math.min(100, value));

  return (
    <div style={{ border: '1px solid #d0d7de', borderRadius: 6, height: 20, width: '100%' }}>
      <div
        style={{
          width: `${boundedValue}%`,
          backgroundColor: '#2da44e',
          height: '100%',
          borderRadius: 6,
          transition: 'width 0.2s ease-in-out'
        }}
      />
    </div>
  );
};
