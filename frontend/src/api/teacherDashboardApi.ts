import { apiGet } from "./client";
import { TeacherDashboardResponse } from "../types/teacherDashboard";

export async function getTeacherDashboard(): Promise<TeacherDashboardResponse> {
  return apiGet<TeacherDashboardResponse>("/teacher/dashboard");
}
