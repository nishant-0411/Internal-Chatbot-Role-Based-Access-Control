---
title: Sales RBAC Hierarchy
department: sales
role_access: marketing,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## Sales Department

The Sales department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Revenue Officer (CRO)

**Role ID:** `RL-SAL-100026`
**Department:** Sales
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Edit Zendesk Support Desk (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- Configure Splunk Security Logs (Full Authorization Verified)
- Destroy Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Erase Staging Environments (Full Authorization Verified)
- Revoke AWS Admin Console (Full Authorization Verified)
- Terminate Snowflake Data Warehouse (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Delete GitHub Enterprise Admin (Full Authorization Verified)
- Remove Kubernetes Production Cluster (Full Authorization Verified)
- Terminate Jira System Admin (Full Authorization Verified)
- Inspect records within Sales Operations
- Inspect records within Sales Operations
- Monitor records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Workday HRIS

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, HubSpot Marketing, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Revenue Officer (CRO) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Revenue Officer (CRO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Chief Revenue Officer (CRO) (Compliance)

**Role ID:** `RL-SAL-100073`
**Department:** Sales
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Alter Salesforce CRM (Full Authorization Verified)
- Drop AWS Admin Console (Full Authorization Verified)
- Remove GCP Core Infrastructure (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Delete Slack Enterprise Grid (Full Authorization Verified)
- Terminate Zendesk Support Desk (Full Authorization Verified)
- Modify GitHub Enterprise Admin (Full Authorization Verified)
- Revoke Jira System Admin (Full Authorization Verified)
- Purge Azure Active Directory (Full Authorization Verified)
- Change Figma Enterprise (Full Authorization Verified)
- Delete Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Destroy Splunk Security Logs (Full Authorization Verified)
- Review records within Sales Operations
- Examine records within Sales Operations
- Access records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Datadog APM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Salesforce CRM, AWS Admin Console, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Revenue Officer (CRO) (Compliance) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Revenue Officer (CRO) (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Chief Revenue Officer (CRO) (Infrastructure)

**Role ID:** `RL-SAL-100023`
**Department:** Sales
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- Revoke Jira System Admin (Full Authorization Verified)
- Erase Salesforce CRM (Full Authorization Verified)
- Remove Zendesk Support Desk (Full Authorization Verified)
- Update Datadog APM (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Tweak MongoDB User Data Store (Full Authorization Verified)
- Purge GCP Core Infrastructure (Full Authorization Verified)
- Drop Snowflake Data Warehouse (Full Authorization Verified)
- Monitor records within Sales Operations
- Inspect records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Slack Enterprise Grid, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Revenue Officer (CRO) (Infrastructure) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Revenue Officer (CRO) (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Chief Revenue Officer (CRO) (Cloud)

**Role ID:** `RL-SAL-100047`
**Department:** Sales
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Delete AWS Admin Console (Full Authorization Verified)
- Remove Kubernetes Production Cluster (Full Authorization Verified)
- Change NetSuite ERP (Full Authorization Verified)
- Change GitHub Enterprise Admin (Full Authorization Verified)
- Revoke Figma Enterprise (Full Authorization Verified)
- Terminate Datadog APM (Full Authorization Verified)
- Destroy Zendesk Support Desk (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Configure MongoDB User Data Store (Full Authorization Verified)
- Erase Workday HRIS (Full Authorization Verified)
- View records within Sales Operations
- Monitor records within Sales Operations
- Consult records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, AWS Admin Console, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Revenue Officer (CRO) (Cloud) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Revenue Officer (CRO) (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Chief Revenue Officer (CRO) (Analytics)

**Role ID:** `RL-SAL-100051`
**Department:** Sales
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Purge Slack Enterprise Grid (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Change MongoDB User Data Store (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Revoke Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Drop Workday HRIS (Full Authorization Verified)
- Modify GCP Core Infrastructure (Full Authorization Verified)
- Terminate Snowflake Data Warehouse (Full Authorization Verified)
- Remove Datadog APM (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect records within Sales Operations
- View records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Salesforce CRM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Azure Active Directory, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Revenue Officer (CRO) (Analytics) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Revenue Officer (CRO) (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### VP of Sales

**Role ID:** `RL-SAL-90010`
**Department:** Sales
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Drop Staging Environments (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Destroy GCP Core Infrastructure (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Remove Jira System Admin (Full Authorization Verified)
- Adjust Workday HRIS (Full Authorization Verified)
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Remove GitHub Enterprise Admin (Full Authorization Verified)
- View records within Sales Operations
- Access records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Snowflake Data Warehouse

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, Datadog APM, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Sales needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Sales receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### VP of Sales (Analytics)

**Role ID:** `RL-SAL-90055`
**Department:** Sales
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Edit Snowflake Data Warehouse (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Destroy Splunk Security Logs (Full Authorization Verified)
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Erase CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Alter AWS Admin Console (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Revoke MongoDB User Data Store (Full Authorization Verified)
- Inspect records within Sales Operations
- Inspect records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Salesforce CRM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Kubernetes Production Cluster, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Sales (Analytics) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Sales (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### VP of Sales (Core)

**Role ID:** `RL-SAL-90071`
**Department:** Sales
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase Zendesk Support Desk (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Delete CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Configure Slack Enterprise Grid (Full Authorization Verified)
- Revoke GCP Core Infrastructure (Full Authorization Verified)
- Drop Figma Enterprise (Full Authorization Verified)
- Destroy MongoDB User Data Store (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Terminate Kubernetes Production Cluster (Full Authorization Verified)
- Review records within Sales Operations
- Examine records within Sales Operations
- Review records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Snowflake Data Warehouse

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, HubSpot Marketing, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Sales (Core) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Sales (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### VP of Sales (Enterprise)

**Role ID:** `RL-SAL-90029`
**Department:** Sales
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak HubSpot Marketing (Full Authorization Verified)
- Modify Zendesk Support Desk (Full Authorization Verified)
- Erase AWS Admin Console (Full Authorization Verified)
- Drop GitHub Enterprise Admin (Full Authorization Verified)
- Update Jira System Admin (Full Authorization Verified)
- Terminate NetSuite ERP (Full Authorization Verified)
- Destroy Kubernetes Production Cluster (Full Authorization Verified)
- Delete Splunk Security Logs (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Delete Workday HRIS (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Audit records within Sales Operations
- Review records within Sales Operations
- Inspect records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing GCP Core Infrastructure

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: HubSpot Marketing, Zendesk Support Desk, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Sales (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Sales (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### VP of Sales (North America)

**Role ID:** `RL-SAL-90019`
**Department:** Sales
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Delete Zendesk Support Desk (Full Authorization Verified)
- Revoke Jira System Admin (Full Authorization Verified)
- Manage AWS Admin Console (Full Authorization Verified)
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Modify CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Remove GCP Core Infrastructure (Full Authorization Verified)
- Delete Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Terminate Staging Environments (Full Authorization Verified)
- Destroy Kubernetes Production Cluster (Full Authorization Verified)
- Review records within Sales Operations
- Monitor records within Sales Operations
- Monitor records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Salesforce CRM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Jira System Admin, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Sales (North America) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Sales (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Sales Director

**Role ID:** `RL-SAL-80015`
**Department:** Sales
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Drop MongoDB User Data Store (Full Authorization Verified)
- Erase Workday HRIS (Full Authorization Verified)
- Erase Azure Active Directory (Full Authorization Verified)
- Revoke Slack Enterprise Grid (Full Authorization Verified)
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Terminate Figma Enterprise (Full Authorization Verified)
- Configure Splunk Security Logs (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Monitor records within Sales Operations
- Inspect records within Sales Operations
- Audit records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Workday HRIS, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Sales Director needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Director receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Sales Director (Enterprise)

**Role ID:** `RL-SAL-80061`
**Department:** Sales
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Revoke Slack Enterprise Grid (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Drop NetSuite ERP (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- Manage Splunk Security Logs (Full Authorization Verified)
- Edit Figma Enterprise (Full Authorization Verified)
- Destroy AWS Admin Console (Full Authorization Verified)
- Drop Workday HRIS (Full Authorization Verified)
- Purge CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Audit records within Sales Operations
- View records within Sales Operations
- View records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Slack Enterprise Grid, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Sales Director (Enterprise) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Director (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Sales Director (EMEA Region)

**Role ID:** `RL-SAL-80047`
**Department:** Sales
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Destroy Datadog APM (Full Authorization Verified)
- Purge AWS Admin Console (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Remove Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Terminate GCP Core Infrastructure (Full Authorization Verified)
- Update Zendesk Support Desk (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Manage Jira System Admin (Full Authorization Verified)
- Consult records within Sales Operations
- Read records within Sales Operations
- Inspect records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, AWS Admin Console, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Sales Director (EMEA Region) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Director (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Sales Director (APAC Region)

**Role ID:** `RL-SAL-80079`
**Department:** Sales
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Erase Datadog APM (Full Authorization Verified)
- Delete Jira System Admin (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Manage Azure Active Directory (Full Authorization Verified)
- Delete Salesforce CRM (Full Authorization Verified)
- Delete GitHub Enterprise Admin (Full Authorization Verified)
- Drop Slack Enterprise Grid (Full Authorization Verified)
- Revoke MongoDB User Data Store (Full Authorization Verified)
- Remove CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Monitor records within Sales Operations
- Monitor records within Sales Operations
- Review records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, Jira System Admin, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Sales Director (APAC Region) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Director (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Sales Director (APAC Region)

**Role ID:** `RL-SAL-80094`
**Department:** Sales
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Erase Figma Enterprise (Full Authorization Verified)
- Modify Workday HRIS (Full Authorization Verified)
- Manage Jira System Admin (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Purge Snowflake Data Warehouse (Full Authorization Verified)
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Erase Slack Enterprise Grid (Full Authorization Verified)
- Read records within Sales Operations
- Read records within Sales Operations
- Audit records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Sales aggregate data.

#### Systems Access
Authorized platforms: Figma Enterprise, Workday HRIS, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Sales Director (APAC Region) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Director (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Sales Manager

**Role ID:** `RL-SAL-70045`
**Department:** Sales
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Change AWS Admin Console (Full Authorization Verified)
- Create Workday HRIS (Full Authorization Verified)
- Modify GitHub Enterprise Admin (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Build Splunk Security Logs (Full Authorization Verified)
- Produce Datadog APM (Full Authorization Verified)
- Build Zendesk Support Desk (Full Authorization Verified)
- Create Azure Active Directory (Full Authorization Verified)
- Build Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Audit records within Sales Operations
- Audit records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Workday HRIS, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Sales Manager needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Sales Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Sales Manager (Core)

**Role ID:** `RL-SAL-70094`
**Department:** Sales
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Manage Staging Environments (Full Authorization Verified)
- Setup Snowflake Data Warehouse (Full Authorization Verified)
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- Modify Datadog APM (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Produce Workday HRIS (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Instantiate GitHub Enterprise Admin (Full Authorization Verified)
- Monitor records within Sales Operations
- View records within Sales Operations
- Review records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Snowflake Data Warehouse, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Sales Manager (Core) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Sales Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Sales Manager (EMEA Region)

**Role ID:** `RL-SAL-70019`
**Department:** Sales
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Staging Environments (Full Authorization Verified)
- Alter Jira System Admin (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Build AWS Admin Console (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- Monitor records within Sales Operations
- Inspect records within Sales Operations
- Monitor records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Jira System Admin, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Sales Manager (EMEA Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Sales Manager (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Sales Manager (Platform)

**Role ID:** `RL-SAL-70058`
**Department:** Sales
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Tweak Splunk Security Logs (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Produce Zendesk Support Desk (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Update AWS Admin Console (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- View records within Sales Operations
- Read records within Sales Operations
- Audit records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, Snowflake Data Warehouse, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Sales Manager (Platform) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Sales Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Sales Manager (North America)

**Role ID:** `RL-SAL-70052`
**Department:** Sales
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Manage NetSuite ERP (Full Authorization Verified)
- Produce Salesforce CRM (Full Authorization Verified)
- Create Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Build Slack Enterprise Grid (Full Authorization Verified)
- Adjust Workday HRIS (Full Authorization Verified)
- Manage Datadog APM (Full Authorization Verified)
- Edit Jira System Admin (Full Authorization Verified)
- Create Zendesk Support Desk (Full Authorization Verified)
- Construct Staging Environments (Full Authorization Verified)
- Read records within Sales Operations
- Read records within Sales Operations
- Review records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, Salesforce CRM, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Sales Manager (North America) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Sales Manager (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Sales Manager

**Role ID:** `RL-SAL-60078`
**Department:** Sales
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Produce Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Generate Figma Enterprise (Full Authorization Verified)
- Setup NetSuite ERP (Full Authorization Verified)
- Setup CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage Zendesk Support Desk (Full Authorization Verified)
- Setup MongoDB User Data Store (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Setup Staging Environments (Full Authorization Verified)
- Read records within Sales Operations
- Consult records within Sales Operations
- Access records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Figma Enterprise, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Sales Manager needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Sales Manager (Enterprise)

**Role ID:** `RL-SAL-60039`
**Department:** Sales
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Construct GitHub Enterprise Admin (Full Authorization Verified)
- Create Kubernetes Production Cluster (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Setup Datadog APM (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Build Workday HRIS (Full Authorization Verified)
- Construct MongoDB User Data Store (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Read records within Sales Operations
- Inspect records within Sales Operations
- View records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Kubernetes Production Cluster, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Sales Manager (Enterprise) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Manager (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Sales Manager (EMEA Region)

**Role ID:** `RL-SAL-60064`
**Department:** Sales
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Manage Zendesk Support Desk (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Configure Splunk Security Logs (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Construct HubSpot Marketing (Full Authorization Verified)
- Adjust Staging Environments (Full Authorization Verified)
- Examine records within Sales Operations
- Inspect records within Sales Operations
- Access records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, NetSuite ERP, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Sales Manager (EMEA Region) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Manager (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Sales Manager (Growth)

**Role ID:** `RL-SAL-60011`
**Department:** Sales
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Setup AWS Admin Console (Full Authorization Verified)
- Produce GitHub Enterprise Admin (Full Authorization Verified)
- Adjust Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Produce Salesforce CRM (Full Authorization Verified)
- Initialize Figma Enterprise (Full Authorization Verified)
- Setup Zendesk Support Desk (Full Authorization Verified)
- Initialize GCP Core Infrastructure (Full Authorization Verified)
- Manage Datadog APM (Full Authorization Verified)
- View records within Sales Operations
- Examine records within Sales Operations
- Monitor records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, GitHub Enterprise Admin, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Sales Manager (Growth) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Sales Manager (Infrastructure)

**Role ID:** `RL-SAL-60058`
**Department:** Sales
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Produce Snowflake Data Warehouse (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Generate Splunk Security Logs (Full Authorization Verified)
- Examine records within Sales Operations
- Audit records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Kubernetes Production Cluster, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Sales Manager (Infrastructure) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Sales Manager (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Regional Sales Lead

**Role ID:** `RL-SAL-50091`
**Department:** Sales
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Produce Workday HRIS (Full Authorization Verified)
- Instantiate Figma Enterprise (Full Authorization Verified)
- Alter Salesforce CRM (Full Authorization Verified)
- Initialize CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Generate GitHub Enterprise Admin (Full Authorization Verified)
- Build AWS Admin Console (Full Authorization Verified)
- Access records within Sales Operations
- Audit records within Sales Operations
- Inspect records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Workday HRIS, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Regional Sales Lead needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Regional Sales Lead (Enterprise)

**Role ID:** `RL-SAL-50083`
**Department:** Sales
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust Snowflake Data Warehouse (Full Authorization Verified)
- Edit Staging Environments (Full Authorization Verified)
- Instantiate Salesforce CRM (Full Authorization Verified)
- Adjust Workday HRIS (Full Authorization Verified)
- Instantiate HubSpot Marketing (Full Authorization Verified)
- Manage GitHub Enterprise Admin (Full Authorization Verified)
- Inspect records within Sales Operations
- View records within Sales Operations
- Monitor records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Snowflake Data Warehouse, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Regional Sales Lead (Enterprise) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Regional Sales Lead (Analytics)

**Role ID:** `RL-SAL-50022`
**Department:** Sales
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Instantiate AWS Admin Console (Full Authorization Verified)
- Construct Salesforce CRM (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Setup HubSpot Marketing (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Examine records within Sales Operations
- Consult records within Sales Operations
- View records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Zendesk Support Desk, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Regional Sales Lead (Analytics) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Regional Sales Lead (Core)

**Role ID:** `RL-SAL-50036`
**Department:** Sales
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Initialize Splunk Security Logs (Full Authorization Verified)
- Configure Staging Environments (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Create Salesforce CRM (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Tweak MongoDB User Data Store (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Consult records within Sales Operations
- Inspect records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, Staging Environments, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Regional Sales Lead (Core) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Regional Sales Lead (North America)

**Role ID:** `RL-SAL-50015`
**Department:** Sales
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Initialize Figma Enterprise (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Manage Jira System Admin (Full Authorization Verified)
- Tweak GitHub Enterprise Admin (Full Authorization Verified)
- Tweak Staging Environments (Full Authorization Verified)
- Generate Slack Enterprise Grid (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Monitor records within Sales Operations
- Monitor records within Sales Operations
- Inspect records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, MongoDB User Data Store, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Regional Sales Lead (North America) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Account Executive

**Role ID:** `RL-SAL-40060`
**Department:** Sales
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Update HubSpot Marketing (Full Authorization Verified)
- Tweak MongoDB User Data Store (Full Authorization Verified)
- Instantiate Zendesk Support Desk (Full Authorization Verified)
- Create Figma Enterprise (Full Authorization Verified)
- Produce Salesforce CRM (Full Authorization Verified)
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Examine records within Sales Operations
- Monitor records within Sales Operations
- Review records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, MongoDB User Data Store, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Account Executive needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Account Executive (Infrastructure)

**Role ID:** `RL-SAL-40061`
**Department:** Sales
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Produce Snowflake Data Warehouse (Full Authorization Verified)
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- Initialize Datadog APM (Full Authorization Verified)
- Setup HubSpot Marketing (Full Authorization Verified)
- Construct Salesforce CRM (Full Authorization Verified)
- Create NetSuite ERP (Full Authorization Verified)
- Read records within Sales Operations
- Access records within Sales Operations
- Read records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, GCP Core Infrastructure, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Account Executive (Infrastructure) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Account Executive (Compliance)

**Role ID:** `RL-SAL-40093`
**Department:** Sales
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Adjust AWS Admin Console (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Instantiate Datadog APM (Full Authorization Verified)
- Consult records within Sales Operations
- Inspect records within Sales Operations
- Access records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), AWS Admin Console, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Account Executive (Compliance) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Account Executive (Growth)

**Role ID:** `RL-SAL-40066`
**Department:** Sales
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Change AWS Admin Console (Full Authorization Verified)
- Construct Jira System Admin (Full Authorization Verified)
- Manage Figma Enterprise (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Update Zendesk Support Desk (Full Authorization Verified)
- Initialize Snowflake Data Warehouse (Full Authorization Verified)
- Examine records within Sales Operations
- Examine records within Sales Operations
- Review records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Jira System Admin, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Account Executive (Growth) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Account Executive (Infrastructure)

**Role ID:** `RL-SAL-40024`
**Department:** Sales
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Generate Snowflake Data Warehouse (Full Authorization Verified)
- Manage Azure Active Directory (Full Authorization Verified)
- Build Slack Enterprise Grid (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Setup Jira System Admin (Full Authorization Verified)
- Produce GitHub Enterprise Admin (Full Authorization Verified)
- Audit records within Sales Operations
- Consult records within Sales Operations
- Monitor records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Azure Active Directory, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Account Executive (Infrastructure) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Account Executive

**Role ID:** `RL-SAL-30027`
**Department:** Sales
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Access Staging Environments (Full Authorization Verified)
- Review AWS Admin Console (Full Authorization Verified)
- Monitor NetSuite ERP (Full Authorization Verified)
- Consult Salesforce CRM (Full Authorization Verified)
- View records within Sales Operations
- Audit records within Sales Operations
- Review records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Staging Environments, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Account Executive needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Account Executive (APAC Region)

**Role ID:** `RL-SAL-30062`
**Department:** Sales
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Azure Active Directory (Full Authorization Verified)
- Monitor Staging Environments (Full Authorization Verified)
- Read Datadog APM (Full Authorization Verified)
- Inspect HubSpot Marketing (Full Authorization Verified)
- Access GitHub Enterprise Admin (Full Authorization Verified)
- Examine records within Sales Operations
- Read records within Sales Operations
- Audit records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Staging Environments, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Account Executive (APAC Region) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Account Executive (Enterprise)

**Role ID:** `RL-SAL-30043`
**Department:** Sales
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit NetSuite ERP (Full Authorization Verified)
- Inspect Slack Enterprise Grid (Full Authorization Verified)
- Monitor Kubernetes Production Cluster (Full Authorization Verified)
- Access GCP Core Infrastructure (Full Authorization Verified)
- Review Datadog APM (Full Authorization Verified)
- View records within Sales Operations
- Review records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, Slack Enterprise Grid, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Account Executive (Enterprise) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Account Executive (Infrastructure)

**Role ID:** `RL-SAL-30069`
**Department:** Sales
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View Zendesk Support Desk (Full Authorization Verified)
- Monitor HubSpot Marketing (Full Authorization Verified)
- Examine Jira System Admin (Full Authorization Verified)
- Consult CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Read Slack Enterprise Grid (Full Authorization Verified)
- Access records within Sales Operations
- View records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, HubSpot Marketing, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Account Executive (Infrastructure) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Account Executive (Compliance)

**Role ID:** `RL-SAL-30015`
**Department:** Sales
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Zendesk Support Desk (Full Authorization Verified)
- Examine Slack Enterprise Grid (Full Authorization Verified)
- Access Jira System Admin (Full Authorization Verified)
- Read Azure Active Directory (Full Authorization Verified)
- Access Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Monitor records within Sales Operations
- Inspect records within Sales Operations
- Review records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Slack Enterprise Grid, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Account Executive (Compliance) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Sales Intern

**Role ID:** `RL-SAL-10076`
**Department:** Sales
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Datadog APM (Full Authorization Verified)
- Inspect MongoDB User Data Store (Full Authorization Verified)
- Consult AWS Admin Console (Full Authorization Verified)
- Review records within Sales Operations
- Consult records within Sales Operations
- Inspect records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, MongoDB User Data Store, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Intern needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Sales Intern (APAC Region)

**Role ID:** `RL-SAL-10021`
**Department:** Sales
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Staging Environments (Full Authorization Verified)
- Inspect Salesforce CRM (Full Authorization Verified)
- Consult GitHub Enterprise Admin (Full Authorization Verified)
- Monitor records within Sales Operations
- View records within Sales Operations
- Audit records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Salesforce CRM, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Intern (APAC Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Sales Intern (Core)

**Role ID:** `RL-SAL-10090`
**Department:** Sales
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Workday HRIS (Full Authorization Verified)
- View CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Audit Snowflake Data Warehouse (Full Authorization Verified)
- Audit records within Sales Operations
- Inspect records within Sales Operations
- Access records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, CI/CD Pipelines (Jenkins/GitHub Actions), Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Intern (Core) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Sales Intern (Enterprise)

**Role ID:** `RL-SAL-10064`
**Department:** Sales
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Jira System Admin (Full Authorization Verified)
- Inspect Staging Environments (Full Authorization Verified)
- Review Splunk Security Logs (Full Authorization Verified)
- Review records within Sales Operations
- Examine records within Sales Operations
- Access records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Staging Environments, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Intern (Enterprise) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Sales Intern (Core)

**Role ID:** `RL-SAL-10083`
**Department:** Sales
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Review Jira System Admin (Full Authorization Verified)
- Examine Workday HRIS (Full Authorization Verified)
- Examine records within Sales Operations
- Audit records within Sales Operations
- Monitor records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Jira System Admin, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Intern (Core) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Sales Consultant

**Role ID:** `RL-SAL-20095`
**Department:** Sales
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Azure Active Directory (Full Authorization Verified)
- Review Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View Kubernetes Production Cluster (Full Authorization Verified)
- Examine Staging Environments (Full Authorization Verified)
- Inspect records within Sales Operations
- View records within Sales Operations
- Inspect records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Production Database Cluster (PostgreSQL), Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Consultant needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Sales Consultant (Analytics)

**Role ID:** `RL-SAL-20055`
**Department:** Sales
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit GitHub Enterprise Admin (Full Authorization Verified)
- View Figma Enterprise (Full Authorization Verified)
- Examine Slack Enterprise Grid (Full Authorization Verified)
- Access Kubernetes Production Cluster (Full Authorization Verified)
- Access records within Sales Operations
- Audit records within Sales Operations
- Read records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Figma Enterprise, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Consultant (Analytics) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Sales Consultant (Infrastructure)

**Role ID:** `RL-SAL-20031`
**Department:** Sales
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Snowflake Data Warehouse (Full Authorization Verified)
- Audit HubSpot Marketing (Full Authorization Verified)
- Monitor AWS Admin Console (Full Authorization Verified)
- Read Salesforce CRM (Full Authorization Verified)
- Access records within Sales Operations
- Audit records within Sales Operations
- Inspect records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, HubSpot Marketing, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Consultant (Infrastructure) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Sales Consultant (Compliance)

**Role ID:** `RL-SAL-20082`
**Department:** Sales
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Splunk Security Logs (Full Authorization Verified)
- Consult MongoDB User Data Store (Full Authorization Verified)
- Examine Workday HRIS (Full Authorization Verified)
- Read Snowflake Data Warehouse (Full Authorization Verified)
- Examine records within Sales Operations
- Inspect records within Sales Operations
- View records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, MongoDB User Data Store, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Consultant (Compliance) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Sales Consultant (Analytics)

**Role ID:** `RL-SAL-20026`
**Department:** Sales
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor MongoDB User Data Store (Full Authorization Verified)
- View Snowflake Data Warehouse (Full Authorization Verified)
- Access NetSuite ERP (Full Authorization Verified)
- Monitor Figma Enterprise (Full Authorization Verified)
- Read records within Sales Operations
- Review records within Sales Operations
- Examine records within Sales Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Sales team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Snowflake Data Warehouse, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Sales Consultant (Analytics) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

