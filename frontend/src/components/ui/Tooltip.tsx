import { ReactNode, useState } from 'react';

type Props = {
  content: ReactNode;
  children: ReactNode;
};

const Tooltip = ({ content, children }: Props): JSX.Element => {
  const [visible, setVisible] = useState(false);

  return (
    <span
      style={{ position: 'relative', display: 'inline-block' }}
      onMouseEnter={() => setVisible(true)}
      onMouseLeave={() => setVisible(false)}
    >
      {children}

      {visible && (
        <div
          style={{
            position: 'absolute',
            bottom: '120%',
            left: '50%',
            transform: 'translateX(-50%)',
            background: '#222',
            color: '#fff',
            padding: '6px 8px',
            borderRadius: 4,
            fontSize: 12,
            whiteSpace: 'nowrap',
            zIndex: 10
          }}
        >
          {content}
        </div>
      )}
    </span>
  );
};

export default Tooltip;