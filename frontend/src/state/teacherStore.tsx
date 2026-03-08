import { createContext, PropsWithChildren, useContext, useMemo, useState } from 'react';

import { AcademicPeriod, StudentId, SubjectGroupId } from '../types/domainTypes';

type TeacherStoreState = {
  selectedSubjectGroup: SubjectGroupId | null;
  selectedStudent: StudentId | null;
  currentAcademicPeriod: AcademicPeriod | null;
  setSelectedSubjectGroup: (groupId: SubjectGroupId | null) => void;
  setSelectedStudent: (studentId: StudentId | null) => void;
  setCurrentAcademicPeriod: (period: AcademicPeriod | null) => void;
};

const TeacherStoreContext = createContext<TeacherStoreState | undefined>(undefined);

export const TeacherStoreProvider = ({ children }: PropsWithChildren): JSX.Element => {
  const [selectedSubjectGroup, setSelectedSubjectGroup] = useState<SubjectGroupId | null>(null);
  const [selectedStudent, setSelectedStudent] = useState<StudentId | null>(null);
  const [currentAcademicPeriod, setCurrentAcademicPeriod] = useState<AcademicPeriod | null>(null);

  const value = useMemo(
    () => ({
      selectedSubjectGroup,
      selectedStudent,
      currentAcademicPeriod,
      setSelectedSubjectGroup,
      setSelectedStudent,
      setCurrentAcademicPeriod
    }),
    [selectedSubjectGroup, selectedStudent, currentAcademicPeriod]
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
