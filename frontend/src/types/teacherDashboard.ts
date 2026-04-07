export interface Indicator {
  indicatorId: string;
  currentStage: number;
  totalStages: number;
  consolidation: number | null;
  normalizedLevel: number | null;
}

export type Competence = {
  competenceId: string;
  competenceName: string;
  indicators: Indicator[];
  averageNormalizedLevel: number | null;
  indicatorCount: number;
};

export type Nucleus = {
  nucleusId: string;
  nucleusName: string;
  competences: Competence[];
  averageNormalizedLevel: number | null;
  competenceCount: number;
};

export interface Student {
  studentId: string;
  studentName: string;
  indicators: Indicator[];
  nucleus: Nucleus[];
}

export interface Group {
  groupId: string;
  groupName: string;
  students: Student[];
}

export interface TeacherDashboardResponse {
  groups: Group[];
  alerts: unknown[];
  period?: unknown;
}
