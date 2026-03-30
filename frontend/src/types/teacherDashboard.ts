export interface Indicator {
  indicatorId: string;
  currentStage: number;
  totalStages: number;
  consolidation: number | null;
  normalizedLevel: number | null;
}

export interface Student {
  studentId: string;
  studentName: string;
  indicators: Indicator[];
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
