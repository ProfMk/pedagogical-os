import { createBrowserRouter, Navigate } from 'react-router-dom';

import { DashboardPage } from '../pages/DashboardPage';
import { GroupPage } from '../pages/GroupPage';
import { IndicatorPage } from '../pages/IndicatorPage';
import { StudentPage } from '../pages/StudentPage';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <Navigate to="/dashboard" replace />
  },
  {
    path: '/dashboard',
    element: <DashboardPage />
  },
  {
    path: '/dashboard/groups/:groupId',
    element: <GroupPage />
  },
  {
    path: '/dashboard/students/:studentId',
    element: <StudentPage />
  },
  {
    path: '/dashboard/indicators/:indicatorId',
    element: <IndicatorPage />
  }
]);
