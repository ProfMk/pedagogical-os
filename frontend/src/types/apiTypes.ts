export type IndicatorProgress = {
  indicatorId: string;
  competencyName?: string;
  indicatorName?: string;
  microStageName?: string;
  currentStage: number;
  totalStages: number;
  consolidation?: number;
  normalizedLevel?: number;
};

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

export interface DashboardSummaryItem {
  id: string;
  label: string;
  value?: number;
}

export interface DashboardApiResponse {
  summary?: string;
  items?: DashboardSummaryItem[];
}

export interface IndicatorApiItem {
  id: string;
  label: string;
}

export interface IndicatorApiResponse {
  indicators: IndicatorApiItem[];
}

export interface StudentApiItem {
  id: string;
  name: string;
}

export interface StudentApiResponse {
  students: StudentApiItem[];
}
