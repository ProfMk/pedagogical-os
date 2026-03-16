import { apiGet } from "./client";
import { TeacherDashboardResponse } from "../types/teacherDashboard";

export async function getTeacherDashboard(
  institutionId: string,
  academicYearId: string
): Promise<TeacherDashboardResponse> {

  return apiGet<TeacherDashboardResponse>(
    `/teacher/dashboard?institution_id=${institutionId}&academic_year_id=${academicYearId}`
  );
}