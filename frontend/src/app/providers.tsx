import { PropsWithChildren } from 'react';

import { TeacherStoreProvider } from '../state/teacherStore';

export const AppProviders = ({ children }: PropsWithChildren): JSX.Element => {
  return <TeacherStoreProvider>{children}</TeacherStoreProvider>;
};
