---
title: Finance RBAC Hierarchy
department: finance
role_access: finance,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## Finance Department

The Finance department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Financial Officer (CFO)

**Role ID:** `RL-FIN-100055`
**Department:** Finance
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak Staging Environments (Full Authorization Verified)
- Destroy Zendesk Support Desk (Full Authorization Verified)
- Remove Jira System Admin (Full Authorization Verified)
- Drop Figma Enterprise (Full Authorization Verified)
- Drop MongoDB User Data Store (Full Authorization Verified)
- Update GCP Core Infrastructure (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Update CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Update Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Audit records within Finance Operations
- Consult records within Finance Operations
- Inspect records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing GitHub Enterprise Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, Zendesk Support Desk, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Financial Officer (CFO) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Financial Officer (CFO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Financial Officer (CFO) (North America)

**Role ID:** `RL-FIN-100044`
**Department:** Finance
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Delete GCP Core Infrastructure (Full Authorization Verified)
- Erase Salesforce CRM (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Remove Workday HRIS (Full Authorization Verified)
- Drop Datadog APM (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Modify AWS Admin Console (Full Authorization Verified)
- Terminate Jira System Admin (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- Purge Slack Enterprise Grid (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Monitor records within Finance Operations
- Inspect records within Finance Operations
- Inspect records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Salesforce CRM, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Financial Officer (CFO) (North America) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Financial Officer (CFO) (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Chief Financial Officer (CFO) (Analytics)

**Role ID:** `RL-FIN-100099`
**Department:** Finance
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase Zendesk Support Desk (Full Authorization Verified)
- Erase Staging Environments (Full Authorization Verified)
- Modify GCP Core Infrastructure (Full Authorization Verified)
- Update Figma Enterprise (Full Authorization Verified)
- Edit Jira System Admin (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Erase Datadog APM (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Revoke Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Remove Snowflake Data Warehouse (Full Authorization Verified)
- Read records within Finance Operations
- Read records within Finance Operations
- Review records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing MongoDB User Data Store

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Staging Environments, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Financial Officer (CFO) (Analytics) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Financial Officer (CFO) (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Financial Officer (CFO) (APAC Region)

**Role ID:** `RL-FIN-100050`
**Department:** Finance
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke GitHub Enterprise Admin (Full Authorization Verified)
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Revoke Salesforce CRM (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Alter Jira System Admin (Full Authorization Verified)
- Purge Staging Environments (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Terminate Figma Enterprise (Full Authorization Verified)
- Alter Zendesk Support Desk (Full Authorization Verified)
- Adjust AWS Admin Console (Full Authorization Verified)
- Read records within Finance Operations
- Examine records within Finance Operations
- Access records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing GCP Core Infrastructure

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, CI/CD Pipelines (Jenkins/GitHub Actions), Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Financial Officer (CFO) (APAC Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Financial Officer (CFO) (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Chief Financial Officer (CFO) (Enterprise)

**Role ID:** `RL-FIN-100030`
**Department:** Finance
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Configure Staging Environments (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Drop AWS Admin Console (Full Authorization Verified)
- Terminate Splunk Security Logs (Full Authorization Verified)
- Revoke Salesforce CRM (Full Authorization Verified)
- Drop Datadog APM (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Consult records within Finance Operations
- Monitor records within Finance Operations
- Read records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), NetSuite ERP, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Financial Officer (CFO) (Enterprise) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Financial Officer (CFO) (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### VP of Finance

**Role ID:** `RL-FIN-90043`
**Department:** Finance
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Edit Jira System Admin (Full Authorization Verified)
- Erase Snowflake Data Warehouse (Full Authorization Verified)
- Terminate Azure Active Directory (Full Authorization Verified)
- Erase AWS Admin Console (Full Authorization Verified)
- Purge CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Modify Workday HRIS (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Manage Kubernetes Production Cluster (Full Authorization Verified)
- Review records within Finance Operations
- Access records within Finance Operations
- Review records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Salesforce CRM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Jira System Admin, Snowflake Data Warehouse, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Finance needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Finance receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### VP of Finance (Infrastructure)

**Role ID:** `RL-FIN-90094`
**Department:** Finance
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase HubSpot Marketing (Full Authorization Verified)
- Delete Staging Environments (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- Purge Kubernetes Production Cluster (Full Authorization Verified)
- Terminate GCP Core Infrastructure (Full Authorization Verified)
- Purge MongoDB User Data Store (Full Authorization Verified)
- Revoke GitHub Enterprise Admin (Full Authorization Verified)
- Remove Azure Active Directory (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Destroy Workday HRIS (Full Authorization Verified)
- Drop Snowflake Data Warehouse (Full Authorization Verified)
- Consult records within Finance Operations
- View records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Jira System Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: HubSpot Marketing, Staging Environments, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Finance (Infrastructure) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Finance (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### VP of Finance (Cloud)

**Role ID:** `RL-FIN-90098`
**Department:** Finance
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Alter Datadog APM (Full Authorization Verified)
- Terminate GCP Core Infrastructure (Full Authorization Verified)
- Revoke CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Purge GitHub Enterprise Admin (Full Authorization Verified)
- Destroy Slack Enterprise Grid (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Remove Zendesk Support Desk (Full Authorization Verified)
- Modify AWS Admin Console (Full Authorization Verified)
- Purge Kubernetes Production Cluster (Full Authorization Verified)
- Erase Snowflake Data Warehouse (Full Authorization Verified)
- Access records within Finance Operations
- Audit records within Finance Operations
- Access records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing MongoDB User Data Store

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, GCP Core Infrastructure, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Finance (Cloud) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Finance (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of Finance (Growth)

**Role ID:** `RL-FIN-90062`
**Department:** Finance
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Edit MongoDB User Data Store (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Edit Snowflake Data Warehouse (Full Authorization Verified)
- Terminate HubSpot Marketing (Full Authorization Verified)
- Manage Zendesk Support Desk (Full Authorization Verified)
- Purge GCP Core Infrastructure (Full Authorization Verified)
- Erase Splunk Security Logs (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Update Staging Environments (Full Authorization Verified)
- Destroy Azure Active Directory (Full Authorization Verified)
- Delete GitHub Enterprise Admin (Full Authorization Verified)
- Consult records within Finance Operations
- Monitor records within Finance Operations
- Monitor records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Kubernetes Production Cluster

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Salesforce CRM, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Finance (Growth) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Finance (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### VP of Finance (North America)

**Role ID:** `RL-FIN-90078`
**Department:** Finance
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak Splunk Security Logs (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Destroy HubSpot Marketing (Full Authorization Verified)
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Erase AWS Admin Console (Full Authorization Verified)
- Adjust Figma Enterprise (Full Authorization Verified)
- Drop GCP Core Infrastructure (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Modify Datadog APM (Full Authorization Verified)
- Examine records within Finance Operations
- Access records within Finance Operations
- Examine records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Azure Active Directory

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Splunk Security Logs, MongoDB User Data Store, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Finance (North America) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Finance (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Director of Finance

**Role ID:** `RL-FIN-80074`
**Department:** Finance
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Terminate Snowflake Data Warehouse (Full Authorization Verified)
- Remove Zendesk Support Desk (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Change Slack Enterprise Grid (Full Authorization Verified)
- Delete AWS Admin Console (Full Authorization Verified)
- Alter NetSuite ERP (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop MongoDB User Data Store (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Remove HubSpot Marketing (Full Authorization Verified)
- Audit records within Finance Operations
- Review records within Finance Operations
- Review records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Zendesk Support Desk, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Finance needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Finance receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Director of Finance (Platform)

**Role ID:** `RL-FIN-80092`
**Department:** Finance
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Change Staging Environments (Full Authorization Verified)
- Change GCP Core Infrastructure (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Delete Datadog APM (Full Authorization Verified)
- Remove HubSpot Marketing (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Destroy Snowflake Data Warehouse (Full Authorization Verified)
- Edit Jira System Admin (Full Authorization Verified)
- Erase AWS Admin Console (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Read records within Finance Operations
- Review records within Finance Operations
- Access records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, GCP Core Infrastructure, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Finance (Platform) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Finance (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Director of Finance (APAC Region)

**Role ID:** `RL-FIN-80096`
**Department:** Finance
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Staging Environments (Full Authorization Verified)
- Destroy Figma Enterprise (Full Authorization Verified)
- Destroy MongoDB User Data Store (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Remove Jira System Admin (Full Authorization Verified)
- Delete Workday HRIS (Full Authorization Verified)
- Revoke GitHub Enterprise Admin (Full Authorization Verified)
- Remove CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Destroy Salesforce CRM (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Consult records within Finance Operations
- Examine records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, Figma Enterprise, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Finance (APAC Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Finance (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Director of Finance (Infrastructure)

**Role ID:** `RL-FIN-80026`
**Department:** Finance
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Adjust Datadog APM (Full Authorization Verified)
- Delete Staging Environments (Full Authorization Verified)
- Destroy Jira System Admin (Full Authorization Verified)
- Delete AWS Admin Console (Full Authorization Verified)
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Delete GCP Core Infrastructure (Full Authorization Verified)
- Revoke MongoDB User Data Store (Full Authorization Verified)
- Erase Zendesk Support Desk (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Purge Snowflake Data Warehouse (Full Authorization Verified)
- Access records within Finance Operations
- Inspect records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, Staging Environments, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Finance (Infrastructure) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Finance (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Director of Finance (Analytics)

**Role ID:** `RL-FIN-80084`
**Department:** Finance
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Alter AWS Admin Console (Full Authorization Verified)
- Destroy Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Remove Staging Environments (Full Authorization Verified)
- Delete Snowflake Data Warehouse (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Manage Azure Active Directory (Full Authorization Verified)
- Drop Salesforce CRM (Full Authorization Verified)
- Update CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Delete NetSuite ERP (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Inspect records within Finance Operations
- Read records within Finance Operations
- Access records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Finance aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, Production Database Cluster (PostgreSQL), Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Finance (Analytics) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Finance (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Finance Manager

**Role ID:** `RL-FIN-70082`
**Department:** Finance
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Change Staging Environments (Full Authorization Verified)
- Change AWS Admin Console (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Produce MongoDB User Data Store (Full Authorization Verified)
- Instantiate Workday HRIS (Full Authorization Verified)
- Construct Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Produce Zendesk Support Desk (Full Authorization Verified)
- Construct Azure Active Directory (Full Authorization Verified)
- Access records within Finance Operations
- View records within Finance Operations
- Review records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, AWS Admin Console, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Finance Manager needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Finance Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Finance Manager (EMEA Region)

**Role ID:** `RL-FIN-70070`
**Department:** Finance
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Slack Enterprise Grid (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Create MongoDB User Data Store (Full Authorization Verified)
- Produce Figma Enterprise (Full Authorization Verified)
- Initialize Zendesk Support Desk (Full Authorization Verified)
- Build Kubernetes Production Cluster (Full Authorization Verified)
- Construct GitHub Enterprise Admin (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- View records within Finance Operations
- Consult records within Finance Operations
- Access records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, HubSpot Marketing, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Finance Manager (EMEA Region) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Finance Manager (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Finance Manager (Enterprise)

**Role ID:** `RL-FIN-70033`
**Department:** Finance
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Initialize Slack Enterprise Grid (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Modify Jira System Admin (Full Authorization Verified)
- Generate GCP Core Infrastructure (Full Authorization Verified)
- Setup Staging Environments (Full Authorization Verified)
- Initialize Azure Active Directory (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Build Workday HRIS (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Access records within Finance Operations
- Consult records within Finance Operations
- Review records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Zendesk Support Desk, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Finance Manager (Enterprise) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Finance Manager (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Finance Manager (Cloud)

**Role ID:** `RL-FIN-70072`
**Department:** Finance
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Setup Figma Enterprise (Full Authorization Verified)
- Generate Splunk Security Logs (Full Authorization Verified)
- Construct Slack Enterprise Grid (Full Authorization Verified)
- Setup Salesforce CRM (Full Authorization Verified)
- Produce Azure Active Directory (Full Authorization Verified)
- Change NetSuite ERP (Full Authorization Verified)
- Modify GCP Core Infrastructure (Full Authorization Verified)
- Alter HubSpot Marketing (Full Authorization Verified)
- Instantiate MongoDB User Data Store (Full Authorization Verified)
- Review records within Finance Operations
- Audit records within Finance Operations
- Examine records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Splunk Security Logs, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Finance Manager (Cloud) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Finance Manager (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Finance Manager (Growth)

**Role ID:** `RL-FIN-70051`
**Department:** Finance
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Produce Workday HRIS (Full Authorization Verified)
- Generate Zendesk Support Desk (Full Authorization Verified)
- Alter Splunk Security Logs (Full Authorization Verified)
- Produce Staging Environments (Full Authorization Verified)
- Initialize Datadog APM (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Instantiate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Generate Kubernetes Production Cluster (Full Authorization Verified)
- Construct Slack Enterprise Grid (Full Authorization Verified)
- Inspect records within Finance Operations
- View records within Finance Operations
- Examine records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Zendesk Support Desk, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Finance Manager (Growth) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Finance Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Finance Manager

**Role ID:** `RL-FIN-60010`
**Department:** Finance
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Update Jira System Admin (Full Authorization Verified)
- Adjust Azure Active Directory (Full Authorization Verified)
- Produce Figma Enterprise (Full Authorization Verified)
- Initialize Staging Environments (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Build Salesforce CRM (Full Authorization Verified)
- Update GCP Core Infrastructure (Full Authorization Verified)
- Consult records within Finance Operations
- Inspect records within Finance Operations
- Examine records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Jira System Admin, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Finance Manager needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Finance Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Finance Manager (Analytics)

**Role ID:** `RL-FIN-60073`
**Department:** Finance
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Update GitHub Enterprise Admin (Full Authorization Verified)
- Instantiate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Adjust Splunk Security Logs (Full Authorization Verified)
- Modify Staging Environments (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Construct Workday HRIS (Full Authorization Verified)
- Initialize NetSuite ERP (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Access records within Finance Operations
- Inspect records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Production Database Cluster (PostgreSQL), Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Finance Manager (Analytics) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Finance Manager (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Finance Manager (Platform)

**Role ID:** `RL-FIN-60090`
**Department:** Finance
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Edit Staging Environments (Full Authorization Verified)
- Initialize Workday HRIS (Full Authorization Verified)
- Configure Datadog APM (Full Authorization Verified)
- Edit Kubernetes Production Cluster (Full Authorization Verified)
- Create Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Generate Splunk Security Logs (Full Authorization Verified)
- Audit records within Finance Operations
- Inspect records within Finance Operations
- Review records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, HubSpot Marketing, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Finance Manager (Platform) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Finance Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Finance Manager (Infrastructure)

**Role ID:** `RL-FIN-60040`
**Department:** Finance
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Instantiate Datadog APM (Full Authorization Verified)
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Produce Zendesk Support Desk (Full Authorization Verified)
- Update Figma Enterprise (Full Authorization Verified)
- Manage Azure Active Directory (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Generate Slack Enterprise Grid (Full Authorization Verified)
- Inspect records within Finance Operations
- Access records within Finance Operations
- Review records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Datadog APM, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Finance Manager (Infrastructure) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Finance Manager (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Finance Manager (Enterprise)

**Role ID:** `RL-FIN-60095`
**Department:** Finance
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Create Figma Enterprise (Full Authorization Verified)
- Adjust GCP Core Infrastructure (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Produce Snowflake Data Warehouse (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Build Workday HRIS (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Audit records within Finance Operations
- Access records within Finance Operations
- Inspect records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, GCP Core Infrastructure, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Finance Manager (Enterprise) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Finance Manager (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Accounting Lead

**Role ID:** `RL-FIN-50097`
**Department:** Finance
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Produce Staging Environments (Full Authorization Verified)
- Generate GitHub Enterprise Admin (Full Authorization Verified)
- Construct Salesforce CRM (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Generate Figma Enterprise (Full Authorization Verified)
- Setup Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Construct Splunk Security Logs (Full Authorization Verified)
- Examine records within Finance Operations
- Read records within Finance Operations
- Access records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, GitHub Enterprise Admin, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Accounting Lead needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Accounting Lead (Platform)

**Role ID:** `RL-FIN-50079`
**Department:** Finance
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Produce AWS Admin Console (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Adjust Staging Environments (Full Authorization Verified)
- Adjust Workday HRIS (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Initialize CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Examine records within Finance Operations
- Examine records within Finance Operations
- Inspect records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, NetSuite ERP, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Accounting Lead (Platform) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Accounting Lead (Cloud)

**Role ID:** `RL-FIN-50098`
**Department:** Finance
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust Figma Enterprise (Full Authorization Verified)
- Manage Datadog APM (Full Authorization Verified)
- Create CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Construct HubSpot Marketing (Full Authorization Verified)
- Alter Jira System Admin (Full Authorization Verified)
- Setup Salesforce CRM (Full Authorization Verified)
- Build Azure Active Directory (Full Authorization Verified)
- Monitor records within Finance Operations
- Inspect records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Datadog APM, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Accounting Lead (Cloud) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Accounting Lead (Platform)

**Role ID:** `RL-FIN-50017`
**Department:** Finance
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Create Snowflake Data Warehouse (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Instantiate Azure Active Directory (Full Authorization Verified)
- Generate Datadog APM (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Manage Figma Enterprise (Full Authorization Verified)
- Examine records within Finance Operations
- View records within Finance Operations
- Examine records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Workday HRIS, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Accounting Lead (Platform) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Accounting Lead (Enterprise)

**Role ID:** `RL-FIN-50077`
**Department:** Finance
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Manage Figma Enterprise (Full Authorization Verified)
- Setup Kubernetes Production Cluster (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Modify Salesforce CRM (Full Authorization Verified)
- Adjust Azure Active Directory (Full Authorization Verified)
- Modify CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Initialize Staging Environments (Full Authorization Verified)
- Inspect records within Finance Operations
- Access records within Finance Operations
- Audit records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Kubernetes Production Cluster, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Accounting Lead (Enterprise) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Financial Analyst

**Role ID:** `RL-FIN-40031`
**Department:** Finance
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Alter AWS Admin Console (Full Authorization Verified)
- Instantiate NetSuite ERP (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Construct Snowflake Data Warehouse (Full Authorization Verified)
- Construct CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Modify Datadog APM (Full Authorization Verified)
- Consult records within Finance Operations
- Access records within Finance Operations
- Audit records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, NetSuite ERP, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Financial Analyst needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Financial Analyst (APAC Region)

**Role ID:** `RL-FIN-40055`
**Department:** Finance
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Change HubSpot Marketing (Full Authorization Verified)
- Manage Jira System Admin (Full Authorization Verified)
- Create AWS Admin Console (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Produce Datadog APM (Full Authorization Verified)
- Setup Azure Active Directory (Full Authorization Verified)
- Consult records within Finance Operations
- Review records within Finance Operations
- Inspect records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Jira System Admin, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Financial Analyst (APAC Region) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Financial Analyst (North America)

**Role ID:** `RL-FIN-40038`
**Department:** Finance
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Initialize Figma Enterprise (Full Authorization Verified)
- Build Azure Active Directory (Full Authorization Verified)
- Update Staging Environments (Full Authorization Verified)
- Generate Slack Enterprise Grid (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Access records within Finance Operations
- Monitor records within Finance Operations
- Access records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Azure Active Directory, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Financial Analyst (North America) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Financial Analyst (Growth)

**Role ID:** `RL-FIN-40051`
**Department:** Finance
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Produce Workday HRIS (Full Authorization Verified)
- Create Azure Active Directory (Full Authorization Verified)
- Manage Kubernetes Production Cluster (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Edit Jira System Admin (Full Authorization Verified)
- Monitor records within Finance Operations
- Monitor records within Finance Operations
- Monitor records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Workday HRIS, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Financial Analyst (Growth) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Financial Analyst (Core)

**Role ID:** `RL-FIN-40050`
**Department:** Finance
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Adjust Staging Environments (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Produce Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Build Kubernetes Production Cluster (Full Authorization Verified)
- Instantiate NetSuite ERP (Full Authorization Verified)
- Construct Slack Enterprise Grid (Full Authorization Verified)
- Access records within Finance Operations
- Inspect records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, GitHub Enterprise Admin, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Financial Analyst (Core) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Financial Analyst

**Role ID:** `RL-FIN-30027`
**Department:** Finance
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Access NetSuite ERP (Full Authorization Verified)
- View Kubernetes Production Cluster (Full Authorization Verified)
- Inspect Splunk Security Logs (Full Authorization Verified)
- Inspect Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Read records within Finance Operations
- Consult records within Finance Operations
- Examine records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), NetSuite ERP, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Analyst needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Financial Analyst (Cloud)

**Role ID:** `RL-FIN-30037`
**Department:** Finance
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Jira System Admin (Full Authorization Verified)
- Access Salesforce CRM (Full Authorization Verified)
- Read Kubernetes Production Cluster (Full Authorization Verified)
- View CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Consult records within Finance Operations
- Monitor records within Finance Operations
- Monitor records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Salesforce CRM, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Analyst (Cloud) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Financial Analyst (North America)

**Role ID:** `RL-FIN-30025`
**Department:** Finance
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Datadog APM (Full Authorization Verified)
- Examine GitHub Enterprise Admin (Full Authorization Verified)
- Monitor Zendesk Support Desk (Full Authorization Verified)
- Monitor Snowflake Data Warehouse (Full Authorization Verified)
- Access MongoDB User Data Store (Full Authorization Verified)
- Audit records within Finance Operations
- Audit records within Finance Operations
- Review records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, GitHub Enterprise Admin, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Analyst (North America) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Financial Analyst (Analytics)

**Role ID:** `RL-FIN-30044`
**Department:** Finance
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Workday HRIS (Full Authorization Verified)
- Review GitHub Enterprise Admin (Full Authorization Verified)
- Audit GCP Core Infrastructure (Full Authorization Verified)
- Review Splunk Security Logs (Full Authorization Verified)
- Examine MongoDB User Data Store (Full Authorization Verified)
- Inspect records within Finance Operations
- Read records within Finance Operations
- Inspect records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, GitHub Enterprise Admin, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Analyst (Analytics) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Financial Analyst (EMEA Region)

**Role ID:** `RL-FIN-30043`
**Department:** Finance
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Splunk Security Logs (Full Authorization Verified)
- View AWS Admin Console (Full Authorization Verified)
- Audit HubSpot Marketing (Full Authorization Verified)
- Read Datadog APM (Full Authorization Verified)
- Monitor GCP Core Infrastructure (Full Authorization Verified)
- Access records within Finance Operations
- Access records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, AWS Admin Console, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Analyst (EMEA Region) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Finance Intern

**Role ID:** `RL-FIN-10044`
**Department:** Finance
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Salesforce CRM (Full Authorization Verified)
- Review Jira System Admin (Full Authorization Verified)
- Access MongoDB User Data Store (Full Authorization Verified)
- Read records within Finance Operations
- View records within Finance Operations
- Monitor records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, Jira System Admin, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Finance Intern needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Finance Intern (Compliance)

**Role ID:** `RL-FIN-10074`
**Department:** Finance
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Jira System Admin (Full Authorization Verified)
- Audit HubSpot Marketing (Full Authorization Verified)
- Access CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Monitor records within Finance Operations
- Examine records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, HubSpot Marketing, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Finance Intern (Compliance) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Finance Intern (Enterprise)

**Role ID:** `RL-FIN-10040`
**Department:** Finance
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine MongoDB User Data Store (Full Authorization Verified)
- Consult Salesforce CRM (Full Authorization Verified)
- Access Jira System Admin (Full Authorization Verified)
- Consult records within Finance Operations
- Review records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Salesforce CRM, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Finance Intern (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Finance Intern (Compliance)

**Role ID:** `RL-FIN-10073`
**Department:** Finance
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult GitHub Enterprise Admin (Full Authorization Verified)
- Access Staging Environments (Full Authorization Verified)
- Audit Zendesk Support Desk (Full Authorization Verified)
- Access records within Finance Operations
- Access records within Finance Operations
- Audit records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Staging Environments, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Finance Intern (Compliance) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Finance Intern (Compliance)

**Role ID:** `RL-FIN-10034`
**Department:** Finance
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access GCP Core Infrastructure (Full Authorization Verified)
- Monitor CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- View Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Read records within Finance Operations
- Audit records within Finance Operations
- Access records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, CI/CD Pipelines (Jenkins/GitHub Actions), Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Finance Intern (Compliance) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Financial Consultant

**Role ID:** `RL-FIN-20022`
**Department:** Finance
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit AWS Admin Console (Full Authorization Verified)
- Inspect GitHub Enterprise Admin (Full Authorization Verified)
- View Staging Environments (Full Authorization Verified)
- Access Azure Active Directory (Full Authorization Verified)
- Access records within Finance Operations
- Access records within Finance Operations
- Read records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, GitHub Enterprise Admin, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Consultant needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Financial Consultant (Core)

**Role ID:** `RL-FIN-20076`
**Department:** Finance
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Staging Environments (Full Authorization Verified)
- Audit Zendesk Support Desk (Full Authorization Verified)
- Audit Workday HRIS (Full Authorization Verified)
- Access GCP Core Infrastructure (Full Authorization Verified)
- Access records within Finance Operations
- Access records within Finance Operations
- Examine records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Zendesk Support Desk, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Consultant (Core) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Financial Consultant (Analytics)

**Role ID:** `RL-FIN-20026`
**Department:** Finance
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Examine Workday HRIS (Full Authorization Verified)
- Access GCP Core Infrastructure (Full Authorization Verified)
- Read NetSuite ERP (Full Authorization Verified)
- Read records within Finance Operations
- Monitor records within Finance Operations
- Consult records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Workday HRIS, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Consultant (Analytics) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Financial Consultant (Infrastructure)

**Role ID:** `RL-FIN-20042`
**Department:** Finance
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit Staging Environments (Full Authorization Verified)
- Read Datadog APM (Full Authorization Verified)
- Access Jira System Admin (Full Authorization Verified)
- Consult Slack Enterprise Grid (Full Authorization Verified)
- Inspect records within Finance Operations
- Examine records within Finance Operations
- Inspect records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Datadog APM, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Consultant (Infrastructure) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Financial Consultant (Growth)

**Role ID:** `RL-FIN-20064`
**Department:** Finance
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult Figma Enterprise (Full Authorization Verified)
- Access Datadog APM (Full Authorization Verified)
- Access MongoDB User Data Store (Full Authorization Verified)
- View Staging Environments (Full Authorization Verified)
- Access records within Finance Operations
- Review records within Finance Operations
- Read records within Finance Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Finance team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Datadog APM, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Financial Consultant (Growth) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

