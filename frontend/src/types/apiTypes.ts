export type IndicatorProgress = {
  indicatorId: string
  competencyName?: string
  indicatorName?: string
  microStageName?: string
  currentStage: number
  totalStages: number
  consolidation?: number
  normalizedLevel?: number
}

export interface StudentDashboard {
  studentId: string;
  studentName: string;
  indicators: IndicatorProgress[];
}

export interface GroupDashboard {
  groupId: string;
  groupName: string;
  students: StudentDashboard[];
}

export interface DashboardAlert {
  indicatorId: string;
  alertType: string;
  affectedStudents: number;
}

export interface TeacherDashboardResponse {
  groups: GroupDashboard[];
  alerts: DashboardAlert[];
}