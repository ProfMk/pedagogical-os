import { createContext, PropsWithChildren, useContext, useMemo, useState } from 'react';

type TeacherStoreState = {
  subjectId: string | null;
  groupId: string | null;
  academicPeriodId: string | null;
  setSubjectId: (subjectId: string | null) => void;
  setGroupId: (groupId: string | null) => void;
  setAcademicPeriodId: (periodId: string | null) => void;
  setSubject: (subjectId: string) => void;
  setGroup: (groupId: string) => void;
  setPeriod: (periodId: string) => void;
};

const TeacherStoreContext = createContext<TeacherStoreState | undefined>(undefined);

export const TeacherStoreProvider = ({ children }: PropsWithChildren): JSX.Element => {
  const [subjectId, setSubjectId] = useState<string | null>(null);
  const [groupId, setGroupId] = useState<string | null>(null);
  const [academicPeriodId, setAcademicPeriodId] = useState<string | null>(null);
  const setSubject = (nextSubjectId: string): void => {
    setSubjectId(nextSubjectId);
    setGroupId(null);
    setAcademicPeriodId(null);
  };
  const setGroup = (nextGroupId: string): void => {
    setGroupId(nextGroupId);
    setAcademicPeriodId(null);
  };
  const setPeriod = (nextPeriodId: string): void => {
    setAcademicPeriodId(nextPeriodId);
  };

  const value = useMemo(
    () => ({
      subjectId,
      groupId,
      academicPeriodId,
      setSubjectId,
      setGroupId,
      setAcademicPeriodId,
      setSubject,
      setGroup,
      setPeriod
    }),
    [subjectId, groupId, academicPeriodId]
  );

  return <TeacherStoreContext.Provider value={value}>{children}</TeacherStoreContext.Provider>;
};

export const useTeacherStore = (): TeacherStoreState => {
  const context = useContext(TeacherStoreContext);
  if (!context) {
    throw new Error('useTeacherStore must be used within a TeacherStoreProvider');
  }

  return context;
};