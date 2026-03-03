---
title: Security RBAC Hierarchy
department: security
role_access: engineering,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## Security Department

The Security department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Information Security Officer (CISO)

**Role ID:** `RL-SEC-100021`
**Department:** Security
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Drop Splunk Security Logs (Full Authorization Verified)
- Remove Figma Enterprise (Full Authorization Verified)
- Delete GitHub Enterprise Admin (Full Authorization Verified)
- Terminate AWS Admin Console (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Change Workday HRIS (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Revoke Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Revoke Kubernetes Production Cluster (Full Authorization Verified)
- Purge Azure Active Directory (Full Authorization Verified)
- Configure Staging Environments (Full Authorization Verified)
- Read records within Security Operations
- Read records within Security Operations
- Inspect records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Jira System Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Splunk Security Logs, Figma Enterprise, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Security Officer (CISO) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Security Officer (CISO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Chief Information Security Officer (CISO) (Compliance)

**Role ID:** `RL-SEC-100076`
**Department:** Security
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Change NetSuite ERP (Full Authorization Verified)
- Edit Snowflake Data Warehouse (Full Authorization Verified)
- Revoke Kubernetes Production Cluster (Full Authorization Verified)
- Remove GCP Core Infrastructure (Full Authorization Verified)
- Revoke MongoDB User Data Store (Full Authorization Verified)
- Modify CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop Zendesk Support Desk (Full Authorization Verified)
- Destroy Slack Enterprise Grid (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Delete HubSpot Marketing (Full Authorization Verified)
- Modify Salesforce CRM (Full Authorization Verified)
- Erase Figma Enterprise (Full Authorization Verified)
- Consult records within Security Operations
- Examine records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Workday HRIS

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: NetSuite ERP, Snowflake Data Warehouse, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Security Officer (CISO) (Compliance) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Security Officer (CISO) (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Chief Information Security Officer (CISO) (Infrastructure)

**Role ID:** `RL-SEC-100070`
**Department:** Security
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak Splunk Security Logs (Full Authorization Verified)
- Configure Salesforce CRM (Full Authorization Verified)
- Purge Azure Active Directory (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- Destroy MongoDB User Data Store (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Delete Slack Enterprise Grid (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Modify GCP Core Infrastructure (Full Authorization Verified)
- Destroy AWS Admin Console (Full Authorization Verified)
- Inspect records within Security Operations
- View records within Security Operations
- Examine records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Jira System Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Splunk Security Logs, Salesforce CRM, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Security Officer (CISO) (Infrastructure) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Security Officer (CISO) (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Chief Information Security Officer (CISO) (Growth)

**Role ID:** `RL-SEC-100053`
**Department:** Security
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak Figma Enterprise (Full Authorization Verified)
- Configure Slack Enterprise Grid (Full Authorization Verified)
- Delete Kubernetes Production Cluster (Full Authorization Verified)
- Update Jira System Admin (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Adjust Staging Environments (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- Delete MongoDB User Data Store (Full Authorization Verified)
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Destroy Azure Active Directory (Full Authorization Verified)
- Destroy GitHub Enterprise Admin (Full Authorization Verified)
- View records within Security Operations
- View records within Security Operations
- Monitor records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Salesforce CRM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Figma Enterprise, Slack Enterprise Grid, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Security Officer (CISO) (Growth) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Security Officer (CISO) (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Chief Information Security Officer (CISO) (Enterprise)

**Role ID:** `RL-SEC-100054`
**Department:** Security
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Modify Workday HRIS (Full Authorization Verified)
- Terminate GCP Core Infrastructure (Full Authorization Verified)
- Purge Slack Enterprise Grid (Full Authorization Verified)
- Change AWS Admin Console (Full Authorization Verified)
- Revoke Jira System Admin (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Erase Salesforce CRM (Full Authorization Verified)
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Manage Splunk Security Logs (Full Authorization Verified)
- Tweak Datadog APM (Full Authorization Verified)
- Monitor records within Security Operations
- Audit records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Zendesk Support Desk

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Workday HRIS, GCP Core Infrastructure, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Security Officer (CISO) (Enterprise) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Security Officer (CISO) (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### VP of Security

**Role ID:** `RL-SEC-90022`
**Department:** Security
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Alter Salesforce CRM (Full Authorization Verified)
- Remove Figma Enterprise (Full Authorization Verified)
- Delete GitHub Enterprise Admin (Full Authorization Verified)
- Destroy Kubernetes Production Cluster (Full Authorization Verified)
- Drop CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop Staging Environments (Full Authorization Verified)
- Terminate Azure Active Directory (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Erase MongoDB User Data Store (Full Authorization Verified)
- Access records within Security Operations
- Read records within Security Operations
- Consult records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Zendesk Support Desk

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Salesforce CRM, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Security needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Security receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of Security (Enterprise)

**Role ID:** `RL-SEC-90013`
**Department:** Security
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Delete Slack Enterprise Grid (Full Authorization Verified)
- Delete NetSuite ERP (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Manage Datadog APM (Full Authorization Verified)
- Erase Jira System Admin (Full Authorization Verified)
- Drop Zendesk Support Desk (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Drop CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Remove Splunk Security Logs (Full Authorization Verified)
- Delete Salesforce CRM (Full Authorization Verified)
- Review records within Security Operations
- Audit records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing GCP Core Infrastructure

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, NetSuite ERP, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Security (Enterprise) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Security (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of Security (Growth)

**Role ID:** `RL-SEC-90077`
**Department:** Security
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Change Azure Active Directory (Full Authorization Verified)
- Edit Snowflake Data Warehouse (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Revoke AWS Admin Console (Full Authorization Verified)
- Update Kubernetes Production Cluster (Full Authorization Verified)
- Terminate Jira System Admin (Full Authorization Verified)
- Terminate Splunk Security Logs (Full Authorization Verified)
- Configure Salesforce CRM (Full Authorization Verified)
- Update GCP Core Infrastructure (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Change MongoDB User Data Store (Full Authorization Verified)
- View records within Security Operations
- Inspect records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Datadog APM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Azure Active Directory, Snowflake Data Warehouse, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Security (Growth) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Security (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### VP of Security (Cloud)

**Role ID:** `RL-SEC-90077`
**Department:** Security
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Remove AWS Admin Console (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Figma Enterprise (Full Authorization Verified)
- Terminate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Delete Splunk Security Logs (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Purge Staging Environments (Full Authorization Verified)
- Delete Snowflake Data Warehouse (Full Authorization Verified)
- Tweak Datadog APM (Full Authorization Verified)
- Change Slack Enterprise Grid (Full Authorization Verified)
- Audit records within Security Operations
- View records within Security Operations
- Inspect records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing GitHub Enterprise Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, HubSpot Marketing, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Security (Cloud) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Security (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### VP of Security (EMEA Region)

**Role ID:** `RL-SEC-90063`
**Department:** Security
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Alter Figma Enterprise (Full Authorization Verified)
- Revoke Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Edit Slack Enterprise Grid (Full Authorization Verified)
- Terminate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Terminate Zendesk Support Desk (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Change Jira System Admin (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Alter AWS Admin Console (Full Authorization Verified)
- Audit records within Security Operations
- Consult records within Security Operations
- Consult records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Workday HRIS

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Figma Enterprise, Production Database Cluster (PostgreSQL), GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Security (EMEA Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Security (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Director of Information Security

**Role ID:** `RL-SEC-80090`
**Department:** Security
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Azure Active Directory (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Destroy Jira System Admin (Full Authorization Verified)
- Delete AWS Admin Console (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Erase Splunk Security Logs (Full Authorization Verified)
- Consult records within Security Operations
- View records within Security Operations
- Examine records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Azure Active Directory, Figma Enterprise, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Information Security needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Information Security receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Director of Information Security (Growth)

**Role ID:** `RL-SEC-80097`
**Department:** Security
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Erase NetSuite ERP (Full Authorization Verified)
- Purge Zendesk Support Desk (Full Authorization Verified)
- Terminate GCP Core Infrastructure (Full Authorization Verified)
- Terminate Salesforce CRM (Full Authorization Verified)
- Adjust Snowflake Data Warehouse (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Remove CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Tweak Workday HRIS (Full Authorization Verified)
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Revoke Figma Enterprise (Full Authorization Verified)
- Audit records within Security Operations
- Consult records within Security Operations
- View records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: NetSuite ERP, Zendesk Support Desk, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Information Security (Growth) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Information Security (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Director of Information Security (Infrastructure)

**Role ID:** `RL-SEC-80048`
**Department:** Security
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Revoke HubSpot Marketing (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change Jira System Admin (Full Authorization Verified)
- Tweak Workday HRIS (Full Authorization Verified)
- Purge AWS Admin Console (Full Authorization Verified)
- Purge Splunk Security Logs (Full Authorization Verified)
- Delete Snowflake Data Warehouse (Full Authorization Verified)
- Purge Figma Enterprise (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Examine records within Security Operations
- Access records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: HubSpot Marketing, CI/CD Pipelines (Jenkins/GitHub Actions), Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Information Security (Infrastructure) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Information Security (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Director of Information Security (EMEA Region)

**Role ID:** `RL-SEC-80018`
**Department:** Security
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Change Azure Active Directory (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Terminate MongoDB User Data Store (Full Authorization Verified)
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Delete CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit Slack Enterprise Grid (Full Authorization Verified)
- Revoke GCP Core Infrastructure (Full Authorization Verified)
- Revoke Kubernetes Production Cluster (Full Authorization Verified)
- Destroy Figma Enterprise (Full Authorization Verified)
- Purge Jira System Admin (Full Authorization Verified)
- Inspect records within Security Operations
- Inspect records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Azure Active Directory, NetSuite ERP, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Information Security (EMEA Region) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Information Security (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Director of Information Security (Compliance)

**Role ID:** `RL-SEC-80042`
**Department:** Security
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Delete Splunk Security Logs (Full Authorization Verified)
- Destroy Kubernetes Production Cluster (Full Authorization Verified)
- Terminate Jira System Admin (Full Authorization Verified)
- Remove Staging Environments (Full Authorization Verified)
- Terminate GCP Core Infrastructure (Full Authorization Verified)
- Manage AWS Admin Console (Full Authorization Verified)
- Erase NetSuite ERP (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Erase Datadog APM (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Audit records within Security Operations
- Examine records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Security aggregate data.

#### Systems Access
Authorized platforms: Splunk Security Logs, Kubernetes Production Cluster, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Information Security (Compliance) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Information Security (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Security Manager

**Role ID:** `RL-SEC-70056`
**Department:** Security
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Setup Azure Active Directory (Full Authorization Verified)
- Update Kubernetes Production Cluster (Full Authorization Verified)
- Build Zendesk Support Desk (Full Authorization Verified)
- Produce Workday HRIS (Full Authorization Verified)
- Instantiate Slack Enterprise Grid (Full Authorization Verified)
- Produce Snowflake Data Warehouse (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Build Figma Enterprise (Full Authorization Verified)
- Modify Salesforce CRM (Full Authorization Verified)
- Read records within Security Operations
- Review records within Security Operations
- Monitor records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Kubernetes Production Cluster, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Security Manager needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Security Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Security Manager (Growth)

**Role ID:** `RL-SEC-70052`
**Department:** Security
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Setup Workday HRIS (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Construct Datadog APM (Full Authorization Verified)
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Manage AWS Admin Console (Full Authorization Verified)
- Manage Zendesk Support Desk (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Inspect records within Security Operations
- Review records within Security Operations
- Examine records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, GitHub Enterprise Admin, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Security Manager (Growth) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Security Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Security Manager (APAC Region)

**Role ID:** `RL-SEC-70047`
**Department:** Security
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Instantiate AWS Admin Console (Full Authorization Verified)
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Create Salesforce CRM (Full Authorization Verified)
- Adjust Staging Environments (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Create GCP Core Infrastructure (Full Authorization Verified)
- Instantiate MongoDB User Data Store (Full Authorization Verified)
- Review records within Security Operations
- View records within Security Operations
- Examine records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Production Database Cluster (PostgreSQL), Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Security Manager (APAC Region) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Security Manager (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Security Manager (Platform)

**Role ID:** `RL-SEC-70051`
**Department:** Security
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Manage MongoDB User Data Store (Full Authorization Verified)
- Produce Azure Active Directory (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Generate Datadog APM (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Configure Salesforce CRM (Full Authorization Verified)
- Instantiate Snowflake Data Warehouse (Full Authorization Verified)
- Construct Workday HRIS (Full Authorization Verified)
- Instantiate GCP Core Infrastructure (Full Authorization Verified)
- View records within Security Operations
- Monitor records within Security Operations
- Consult records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Azure Active Directory, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Security Manager (Platform) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Security Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Security Manager (Infrastructure)

**Role ID:** `RL-SEC-70036`
**Department:** Security
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Update Datadog APM (Full Authorization Verified)
- Produce HubSpot Marketing (Full Authorization Verified)
- Change MongoDB User Data Store (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Update Splunk Security Logs (Full Authorization Verified)
- Instantiate Kubernetes Production Cluster (Full Authorization Verified)
- Build Slack Enterprise Grid (Full Authorization Verified)
- Setup Staging Environments (Full Authorization Verified)
- Manage AWS Admin Console (Full Authorization Verified)
- Inspect records within Security Operations
- Read records within Security Operations
- Consult records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, HubSpot Marketing, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Security Manager (Infrastructure) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Security Manager (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Security Manager

**Role ID:** `RL-SEC-60074`
**Department:** Security
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Modify GitHub Enterprise Admin (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Produce Slack Enterprise Grid (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Setup Zendesk Support Desk (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- View records within Security Operations
- View records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Datadog APM, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Security Manager needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Security Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Security Manager (Platform)

**Role ID:** `RL-SEC-60083`
**Department:** Security
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Produce Workday HRIS (Full Authorization Verified)
- Instantiate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Configure Datadog APM (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Build Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Access records within Security Operations
- Read records within Security Operations
- Access records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, CI/CD Pipelines (Jenkins/GitHub Actions), Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Security Manager (Platform) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Security Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Security Manager (EMEA Region)

**Role ID:** `RL-SEC-60041`
**Department:** Security
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust Salesforce CRM (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Adjust Figma Enterprise (Full Authorization Verified)
- Build Kubernetes Production Cluster (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Generate Azure Active Directory (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Read records within Security Operations
- Review records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, MongoDB User Data Store, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Security Manager (EMEA Region) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Security Manager (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Security Manager (Cloud)

**Role ID:** `RL-SEC-60031`
**Department:** Security
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Construct MongoDB User Data Store (Full Authorization Verified)
- Construct Kubernetes Production Cluster (Full Authorization Verified)
- Modify HubSpot Marketing (Full Authorization Verified)
- Initialize AWS Admin Console (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Modify Staging Environments (Full Authorization Verified)
- Setup Figma Enterprise (Full Authorization Verified)
- Initialize CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Monitor records within Security Operations
- Review records within Security Operations
- Review records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Kubernetes Production Cluster, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Security Manager (Cloud) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Security Manager (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Security Manager (Core)

**Role ID:** `RL-SEC-60066`
**Department:** Security
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Modify Jira System Admin (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Tweak Figma Enterprise (Full Authorization Verified)
- Construct Zendesk Support Desk (Full Authorization Verified)
- Setup GitHub Enterprise Admin (Full Authorization Verified)
- Edit Snowflake Data Warehouse (Full Authorization Verified)
- Create Workday HRIS (Full Authorization Verified)
- Audit records within Security Operations
- Review records within Security Operations
- Examine records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Datadog APM, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Security Manager (Core) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Security Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### SOC Lead

**Role ID:** `RL-SEC-50063`
**Department:** Security
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Produce Figma Enterprise (Full Authorization Verified)
- Edit AWS Admin Console (Full Authorization Verified)
- Adjust Jira System Admin (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Read records within Security Operations
- Consult records within Security Operations
- Consult records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), GitHub Enterprise Admin, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A SOC Lead needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### SOC Lead (Analytics)

**Role ID:** `RL-SEC-50092`
**Department:** Security
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Instantiate Splunk Security Logs (Full Authorization Verified)
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Modify GitHub Enterprise Admin (Full Authorization Verified)
- Generate Workday HRIS (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Generate Salesforce CRM (Full Authorization Verified)
- Review records within Security Operations
- Monitor records within Security Operations
- Review records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, Production Database Cluster (PostgreSQL), NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A SOC Lead (Analytics) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### SOC Lead (EMEA Region)

**Role ID:** `RL-SEC-50014`
**Department:** Security
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- Create Kubernetes Production Cluster (Full Authorization Verified)
- Update GitHub Enterprise Admin (Full Authorization Verified)
- Tweak Jira System Admin (Full Authorization Verified)
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Consult records within Security Operations
- View records within Security Operations
- Inspect records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Kubernetes Production Cluster, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A SOC Lead (EMEA Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### SOC Lead (Compliance)

**Role ID:** `RL-SEC-50029`
**Department:** Security
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Create Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Modify Salesforce CRM (Full Authorization Verified)
- Change Jira System Admin (Full Authorization Verified)
- Adjust Azure Active Directory (Full Authorization Verified)
- Create AWS Admin Console (Full Authorization Verified)
- Review records within Security Operations
- Monitor records within Security Operations
- Access records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), HubSpot Marketing, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A SOC Lead (Compliance) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### SOC Lead (Platform)

**Role ID:** `RL-SEC-50034`
**Department:** Security
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Modify Staging Environments (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Create Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Construct Zendesk Support Desk (Full Authorization Verified)
- Instantiate Figma Enterprise (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Create HubSpot Marketing (Full Authorization Verified)
- Consult records within Security Operations
- Consult records within Security Operations
- View records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Salesforce CRM, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A SOC Lead (Platform) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Security Engineer

**Role ID:** `RL-SEC-40049`
**Department:** Security
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Edit NetSuite ERP (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Setup GitHub Enterprise Admin (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Access records within Security Operations
- Read records within Security Operations
- Inspect records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, Salesforce CRM, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Security Engineer needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Security Engineer (Analytics)

**Role ID:** `RL-SEC-40043`
**Department:** Security
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Generate HubSpot Marketing (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Build Workday HRIS (Full Authorization Verified)
- Instantiate Datadog APM (Full Authorization Verified)
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Instantiate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Monitor records within Security Operations
- Consult records within Security Operations
- Inspect records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Kubernetes Production Cluster, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Security Engineer (Analytics) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Security Engineer (Growth)

**Role ID:** `RL-SEC-40010`
**Department:** Security
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Generate MongoDB User Data Store (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Generate Kubernetes Production Cluster (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Configure Slack Enterprise Grid (Full Authorization Verified)
- Inspect records within Security Operations
- View records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, CI/CD Pipelines (Jenkins/GitHub Actions), Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Security Engineer (Growth) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Security Engineer (Cloud)

**Role ID:** `RL-SEC-40096`
**Department:** Security
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Adjust GCP Core Infrastructure (Full Authorization Verified)
- Tweak Staging Environments (Full Authorization Verified)
- Build Datadog APM (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Create Slack Enterprise Grid (Full Authorization Verified)
- Update Jira System Admin (Full Authorization Verified)
- View records within Security Operations
- Consult records within Security Operations
- Consult records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Staging Environments, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Security Engineer (Cloud) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Security Engineer (Analytics)

**Role ID:** `RL-SEC-40094`
**Department:** Security
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Build GitHub Enterprise Admin (Full Authorization Verified)
- Initialize Zendesk Support Desk (Full Authorization Verified)
- Generate Datadog APM (Full Authorization Verified)
- Build Workday HRIS (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Examine records within Security Operations
- Examine records within Security Operations
- Review records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Zendesk Support Desk, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Security Engineer (Analytics) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Security Analyst

**Role ID:** `RL-SEC-30037`
**Department:** Security
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View GitHub Enterprise Admin (Full Authorization Verified)
- Consult Jira System Admin (Full Authorization Verified)
- Review Azure Active Directory (Full Authorization Verified)
- Access CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Audit Staging Environments (Full Authorization Verified)
- Access records within Security Operations
- View records within Security Operations
- Inspect records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Jira System Admin, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Analyst needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Security Analyst (Growth)

**Role ID:** `RL-SEC-30043`
**Department:** Security
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Figma Enterprise (Full Authorization Verified)
- View Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Review Kubernetes Production Cluster (Full Authorization Verified)
- Examine HubSpot Marketing (Full Authorization Verified)
- Monitor CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- View records within Security Operations
- Inspect records within Security Operations
- Audit records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Production Database Cluster (PostgreSQL), Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Analyst (Growth) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Security Analyst (Cloud)

**Role ID:** `RL-SEC-30092`
**Department:** Security
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Slack Enterprise Grid (Full Authorization Verified)
- Examine Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Read MongoDB User Data Store (Full Authorization Verified)
- View Workday HRIS (Full Authorization Verified)
- Examine Jira System Admin (Full Authorization Verified)
- Review records within Security Operations
- Monitor records within Security Operations
- Monitor records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Production Database Cluster (PostgreSQL), MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Analyst (Cloud) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Security Analyst (Growth)

**Role ID:** `RL-SEC-30012`
**Department:** Security
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Workday HRIS (Full Authorization Verified)
- Monitor Azure Active Directory (Full Authorization Verified)
- Monitor MongoDB User Data Store (Full Authorization Verified)
- View AWS Admin Console (Full Authorization Verified)
- Inspect Splunk Security Logs (Full Authorization Verified)
- Access records within Security Operations
- Read records within Security Operations
- View records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Azure Active Directory, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Analyst (Growth) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Security Analyst (Core)

**Role ID:** `RL-SEC-30072`
**Department:** Security
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access GitHub Enterprise Admin (Full Authorization Verified)
- Access Figma Enterprise (Full Authorization Verified)
- Read Datadog APM (Full Authorization Verified)
- Access Jira System Admin (Full Authorization Verified)
- Examine Slack Enterprise Grid (Full Authorization Verified)
- Monitor records within Security Operations
- Read records within Security Operations
- Consult records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Figma Enterprise, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Analyst (Core) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Security Intern

**Role ID:** `RL-SEC-10092`
**Department:** Security
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review GCP Core Infrastructure (Full Authorization Verified)
- Examine Azure Active Directory (Full Authorization Verified)
- Examine Datadog APM (Full Authorization Verified)
- Examine records within Security Operations
- Audit records within Security Operations
- Examine records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Azure Active Directory, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Intern needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Security Intern (Compliance)

**Role ID:** `RL-SEC-10067`
**Department:** Security
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit Staging Environments (Full Authorization Verified)
- Access MongoDB User Data Store (Full Authorization Verified)
- Audit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Examine records within Security Operations
- Examine records within Security Operations
- Access records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, MongoDB User Data Store, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Intern (Compliance) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Security Intern (North America)

**Role ID:** `RL-SEC-10045`
**Department:** Security
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View Splunk Security Logs (Full Authorization Verified)
- Monitor Kubernetes Production Cluster (Full Authorization Verified)
- Review Datadog APM (Full Authorization Verified)
- Access records within Security Operations
- View records within Security Operations
- View records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, Kubernetes Production Cluster, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Intern (North America) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Security Intern (Cloud)

**Role ID:** `RL-SEC-10051`
**Department:** Security
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit Jira System Admin (Full Authorization Verified)
- Access NetSuite ERP (Full Authorization Verified)
- View Kubernetes Production Cluster (Full Authorization Verified)
- Review records within Security Operations
- Audit records within Security Operations
- Review records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, NetSuite ERP, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Intern (Cloud) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Security Intern (Platform)

**Role ID:** `RL-SEC-10016`
**Department:** Security
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Slack Enterprise Grid (Full Authorization Verified)
- Review Kubernetes Production Cluster (Full Authorization Verified)
- Read Azure Active Directory (Full Authorization Verified)
- View records within Security Operations
- Review records within Security Operations
- Inspect records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Kubernetes Production Cluster, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Intern (Platform) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Security Auditor

**Role ID:** `RL-SEC-20058`
**Department:** Security
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Figma Enterprise (Full Authorization Verified)
- Access Zendesk Support Desk (Full Authorization Verified)
- Monitor AWS Admin Console (Full Authorization Verified)
- Read Azure Active Directory (Full Authorization Verified)
- View records within Security Operations
- Examine records within Security Operations
- Monitor records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Zendesk Support Desk, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Auditor needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Security Auditor (Growth)

**Role ID:** `RL-SEC-20034`
**Department:** Security
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine HubSpot Marketing (Full Authorization Verified)
- Read Figma Enterprise (Full Authorization Verified)
- Examine Slack Enterprise Grid (Full Authorization Verified)
- Review Staging Environments (Full Authorization Verified)
- Audit records within Security Operations
- Review records within Security Operations
- Read records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Figma Enterprise, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Auditor (Growth) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Security Auditor (EMEA Region)

**Role ID:** `RL-SEC-20025`
**Department:** Security
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Review AWS Admin Console (Full Authorization Verified)
- View NetSuite ERP (Full Authorization Verified)
- Examine Kubernetes Production Cluster (Full Authorization Verified)
- View records within Security Operations
- View records within Security Operations
- Inspect records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), AWS Admin Console, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Auditor (EMEA Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Security Auditor (Infrastructure)

**Role ID:** `RL-SEC-20056`
**Department:** Security
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View GCP Core Infrastructure (Full Authorization Verified)
- Consult Azure Active Directory (Full Authorization Verified)
- Examine Datadog APM (Full Authorization Verified)
- Inspect MongoDB User Data Store (Full Authorization Verified)
- Read records within Security Operations
- Audit records within Security Operations
- Inspect records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Azure Active Directory, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Auditor (Infrastructure) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Security Auditor (Core)

**Role ID:** `RL-SEC-20051`
**Department:** Security
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit Jira System Admin (Full Authorization Verified)
- Monitor HubSpot Marketing (Full Authorization Verified)
- Read Zendesk Support Desk (Full Authorization Verified)
- Read NetSuite ERP (Full Authorization Verified)
- Read records within Security Operations
- Read records within Security Operations
- Monitor records within Security Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Security team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, HubSpot Marketing, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Security Auditor (Core) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

