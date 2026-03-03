---
title: Data Science RBAC Hierarchy
department: data science
role_access: engineering,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## Data Science Department

The Data Science department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Data Officer (CDO)

**Role ID:** `RL-DAT-100024`
**Department:** Data Science
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Drop Zendesk Support Desk (Full Authorization Verified)
- Edit Kubernetes Production Cluster (Full Authorization Verified)
- Drop GitHub Enterprise Admin (Full Authorization Verified)
- Erase CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Revoke Splunk Security Logs (Full Authorization Verified)
- Tweak Staging Environments (Full Authorization Verified)
- Terminate Datadog APM (Full Authorization Verified)
- Destroy Snowflake Data Warehouse (Full Authorization Verified)
- Delete HubSpot Marketing (Full Authorization Verified)
- Alter Workday HRIS (Full Authorization Verified)
- Inspect records within Data Science Operations
- Monitor records within Data Science Operations
- Review records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Slack Enterprise Grid

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Zendesk Support Desk, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Data Officer (CDO) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Data Officer (CDO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Data Officer (CDO) (Analytics)

**Role ID:** `RL-DAT-100028`
**Department:** Data Science
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Destroy HubSpot Marketing (Full Authorization Verified)
- Revoke GCP Core Infrastructure (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Manage Jira System Admin (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Destroy CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Manage Splunk Security Logs (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Purge Workday HRIS (Full Authorization Verified)
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Review records within Data Science Operations
- Audit records within Data Science Operations
- View records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Staging Environments

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, HubSpot Marketing, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Data Officer (CDO) (Analytics) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Data Officer (CDO) (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Data Officer (CDO) (APAC Region)

**Role ID:** `RL-DAT-100048`
**Department:** Data Science
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Destroy Snowflake Data Warehouse (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Remove Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Manage Jira System Admin (Full Authorization Verified)
- Destroy Staging Environments (Full Authorization Verified)
- Change Slack Enterprise Grid (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Alter Workday HRIS (Full Authorization Verified)
- Delete Figma Enterprise (Full Authorization Verified)
- Erase MongoDB User Data Store (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Access records within Data Science Operations
- Consult records within Data Science Operations
- Read records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing HubSpot Marketing

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, NetSuite ERP, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Data Officer (CDO) (APAC Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Data Officer (CDO) (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Data Officer (CDO) (Analytics)

**Role ID:** `RL-DAT-100044`
**Department:** Data Science
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Remove AWS Admin Console (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Update Figma Enterprise (Full Authorization Verified)
- Revoke Azure Active Directory (Full Authorization Verified)
- Modify Staging Environments (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Purge MongoDB User Data Store (Full Authorization Verified)
- Delete Splunk Security Logs (Full Authorization Verified)
- Update Jira System Admin (Full Authorization Verified)
- Erase CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Review records within Data Science Operations
- Inspect records within Data Science Operations
- Audit records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Workday HRIS

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, Datadog APM, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Data Officer (CDO) (Analytics) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Data Officer (CDO) (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Chief Data Officer (CDO) (EMEA Region)

**Role ID:** `RL-DAT-100081`
**Department:** Data Science
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Adjust CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop Staging Environments (Full Authorization Verified)
- Remove GitHub Enterprise Admin (Full Authorization Verified)
- Destroy Slack Enterprise Grid (Full Authorization Verified)
- Drop Snowflake Data Warehouse (Full Authorization Verified)
- Drop Datadog APM (Full Authorization Verified)
- Tweak Salesforce CRM (Full Authorization Verified)
- Drop MongoDB User Data Store (Full Authorization Verified)
- Terminate HubSpot Marketing (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Update GCP Core Infrastructure (Full Authorization Verified)
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Access records within Data Science Operations
- View records within Data Science Operations
- Inspect records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Jira System Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Staging Environments, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Data Officer (CDO) (EMEA Region) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Data Officer (CDO) (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of Data Science

**Role ID:** `RL-DAT-90028`
**Department:** Data Science
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Manage CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Remove Workday HRIS (Full Authorization Verified)
- Configure MongoDB User Data Store (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Manage Kubernetes Production Cluster (Full Authorization Verified)
- Remove GitHub Enterprise Admin (Full Authorization Verified)
- Erase Snowflake Data Warehouse (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Revoke Splunk Security Logs (Full Authorization Verified)
- Manage AWS Admin Console (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Access records within Data Science Operations
- Audit records within Data Science Operations
- Audit records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Workday HRIS, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Data Science needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Data Science receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### VP of Data Science (Growth)

**Role ID:** `RL-DAT-90020`
**Department:** Data Science
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Destroy GCP Core Infrastructure (Full Authorization Verified)
- Terminate HubSpot Marketing (Full Authorization Verified)
- Drop MongoDB User Data Store (Full Authorization Verified)
- Destroy CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage Workday HRIS (Full Authorization Verified)
- Remove Splunk Security Logs (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Purge Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Revoke GitHub Enterprise Admin (Full Authorization Verified)
- Audit records within Data Science Operations
- Examine records within Data Science Operations
- View records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Slack Enterprise Grid

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, HubSpot Marketing, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Data Science (Growth) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Data Science (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### VP of Data Science (Enterprise)

**Role ID:** `RL-DAT-90019`
**Department:** Data Science
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Adjust Datadog APM (Full Authorization Verified)
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Configure Splunk Security Logs (Full Authorization Verified)
- Modify Staging Environments (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Edit Jira System Admin (Full Authorization Verified)
- Change Workday HRIS (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Purge AWS Admin Console (Full Authorization Verified)
- Alter Zendesk Support Desk (Full Authorization Verified)
- Update Azure Active Directory (Full Authorization Verified)
- Monitor records within Data Science Operations
- Inspect records within Data Science Operations
- View records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing GCP Core Infrastructure

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, Production Database Cluster (PostgreSQL), Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Data Science (Enterprise) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Data Science (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### VP of Data Science (Cloud)

**Role ID:** `RL-DAT-90077`
**Department:** Data Science
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage Azure Active Directory (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Adjust Jira System Admin (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Update Datadog APM (Full Authorization Verified)
- Drop Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Purge Snowflake Data Warehouse (Full Authorization Verified)
- Adjust Splunk Security Logs (Full Authorization Verified)
- Audit records within Data Science Operations
- Consult records within Data Science Operations
- Access records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Slack Enterprise Grid

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Azure Active Directory, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Data Science (Cloud) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Data Science (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### VP of Data Science (North America)

**Role ID:** `RL-DAT-90031`
**Department:** Data Science
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Change Workday HRIS (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Alter AWS Admin Console (Full Authorization Verified)
- Delete Datadog APM (Full Authorization Verified)
- Manage GitHub Enterprise Admin (Full Authorization Verified)
- Configure Azure Active Directory (Full Authorization Verified)
- Terminate Jira System Admin (Full Authorization Verified)
- Revoke GCP Core Infrastructure (Full Authorization Verified)
- Revoke Splunk Security Logs (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Read records within Data Science Operations
- Audit records within Data Science Operations
- Review records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing HubSpot Marketing

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Workday HRIS, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Data Science (North America) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Data Science (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Director of Data Science

**Role ID:** `RL-DAT-80092`
**Department:** Data Science
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Erase MongoDB User Data Store (Full Authorization Verified)
- Change GCP Core Infrastructure (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Edit AWS Admin Console (Full Authorization Verified)
- Remove Staging Environments (Full Authorization Verified)
- Remove Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Remove Kubernetes Production Cluster (Full Authorization Verified)
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Purge Zendesk Support Desk (Full Authorization Verified)
- Access records within Data Science Operations
- Monitor records within Data Science Operations
- View records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, MongoDB User Data Store, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Data Science needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Data Science receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Director of Data Science (Analytics)

**Role ID:** `RL-DAT-80041`
**Department:** Data Science
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Erase Snowflake Data Warehouse (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Drop NetSuite ERP (Full Authorization Verified)
- Erase Staging Environments (Full Authorization Verified)
- Update GitHub Enterprise Admin (Full Authorization Verified)
- Remove Slack Enterprise Grid (Full Authorization Verified)
- Drop Datadog APM (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Delete Kubernetes Production Cluster (Full Authorization Verified)
- View records within Data Science Operations
- Consult records within Data Science Operations
- Inspect records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Salesforce CRM, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Data Science (Analytics) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Data Science (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Director of Data Science (Analytics)

**Role ID:** `RL-DAT-80059`
**Department:** Data Science
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Destroy Figma Enterprise (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Edit Datadog APM (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Adjust Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Alter Workday HRIS (Full Authorization Verified)
- Remove Jira System Admin (Full Authorization Verified)
- Revoke Azure Active Directory (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Erase Slack Enterprise Grid (Full Authorization Verified)
- Access records within Data Science Operations
- View records within Data Science Operations
- View records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: Figma Enterprise, MongoDB User Data Store, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Data Science (Analytics) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Data Science (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Director of Data Science (APAC Region)

**Role ID:** `RL-DAT-80032`
**Department:** Data Science
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Revoke CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Remove Slack Enterprise Grid (Full Authorization Verified)
- Destroy Kubernetes Production Cluster (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Adjust Splunk Security Logs (Full Authorization Verified)
- Delete Snowflake Data Warehouse (Full Authorization Verified)
- Delete MongoDB User Data Store (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Modify Staging Environments (Full Authorization Verified)
- Consult records within Data Science Operations
- Review records within Data Science Operations
- Examine records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Production Database Cluster (PostgreSQL), Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Data Science (APAC Region) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Data Science (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Director of Data Science (Growth)

**Role ID:** `RL-DAT-80064`
**Department:** Data Science
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Destroy CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop NetSuite ERP (Full Authorization Verified)
- Revoke Splunk Security Logs (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Terminate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Destroy GitHub Enterprise Admin (Full Authorization Verified)
- Purge Slack Enterprise Grid (Full Authorization Verified)
- Terminate Jira System Admin (Full Authorization Verified)
- Manage Azure Active Directory (Full Authorization Verified)
- Inspect records within Data Science Operations
- Review records within Data Science Operations
- Consult records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Data Science aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, CI/CD Pipelines (Jenkins/GitHub Actions), NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Data Science (Growth) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Data Science (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Data Science Manager

**Role ID:** `RL-DAT-70032`
**Department:** Data Science
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Setup Salesforce CRM (Full Authorization Verified)
- Manage Jira System Admin (Full Authorization Verified)
- Modify Datadog APM (Full Authorization Verified)
- Construct Azure Active Directory (Full Authorization Verified)
- Create Zendesk Support Desk (Full Authorization Verified)
- Initialize Splunk Security Logs (Full Authorization Verified)
- Construct NetSuite ERP (Full Authorization Verified)
- Adjust Workday HRIS (Full Authorization Verified)
- Initialize Staging Environments (Full Authorization Verified)
- Examine records within Data Science Operations
- Examine records within Data Science Operations
- Audit records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, Jira System Admin, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Data Science Manager needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Data Science Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Data Science Manager (Growth)

**Role ID:** `RL-DAT-70043`
**Department:** Data Science
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Alter Datadog APM (Full Authorization Verified)
- Update Figma Enterprise (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Setup NetSuite ERP (Full Authorization Verified)
- Modify CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Produce Snowflake Data Warehouse (Full Authorization Verified)
- Examine records within Data Science Operations
- Consult records within Data Science Operations
- Monitor records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, Figma Enterprise, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Data Science Manager (Growth) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Data Science Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Data Science Manager (North America)

**Role ID:** `RL-DAT-70088`
**Department:** Data Science
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Initialize Azure Active Directory (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Build Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Manage Zendesk Support Desk (Full Authorization Verified)
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Generate Kubernetes Production Cluster (Full Authorization Verified)
- Setup GCP Core Infrastructure (Full Authorization Verified)
- Instantiate Figma Enterprise (Full Authorization Verified)
- Read records within Data Science Operations
- Access records within Data Science Operations
- Review records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, GitHub Enterprise Admin, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Data Science Manager (North America) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Data Science Manager (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Data Science Manager (EMEA Region)

**Role ID:** `RL-DAT-70079`
**Department:** Data Science
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Initialize Splunk Security Logs (Full Authorization Verified)
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Construct Jira System Admin (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Produce AWS Admin Console (Full Authorization Verified)
- Initialize Snowflake Data Warehouse (Full Authorization Verified)
- Create GitHub Enterprise Admin (Full Authorization Verified)
- Access records within Data Science Operations
- Monitor records within Data Science Operations
- Audit records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, GCP Core Infrastructure, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Data Science Manager (EMEA Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Data Science Manager (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Data Science Manager (North America)

**Role ID:** `RL-DAT-70064`
**Department:** Data Science
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Tweak Salesforce CRM (Full Authorization Verified)
- Adjust GCP Core Infrastructure (Full Authorization Verified)
- Generate GitHub Enterprise Admin (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Update AWS Admin Console (Full Authorization Verified)
- Construct Zendesk Support Desk (Full Authorization Verified)
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Initialize CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect records within Data Science Operations
- Inspect records within Data Science Operations
- Access records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, GCP Core Infrastructure, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Data Science Manager (North America) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Data Science Manager (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Data Science Manager

**Role ID:** `RL-DAT-60075`
**Department:** Data Science
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Modify Figma Enterprise (Full Authorization Verified)
- Generate Kubernetes Production Cluster (Full Authorization Verified)
- Configure Datadog APM (Full Authorization Verified)
- Update CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Construct GitHub Enterprise Admin (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Inspect records within Data Science Operations
- Consult records within Data Science Operations
- Inspect records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Kubernetes Production Cluster, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Data Science Manager needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Data Science Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Data Science Manager (Platform)

**Role ID:** `RL-DAT-60095`
**Department:** Data Science
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Configure Splunk Security Logs (Full Authorization Verified)
- Alter AWS Admin Console (Full Authorization Verified)
- Generate Snowflake Data Warehouse (Full Authorization Verified)
- Build HubSpot Marketing (Full Authorization Verified)
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Tweak Workday HRIS (Full Authorization Verified)
- Update Datadog APM (Full Authorization Verified)
- Examine records within Data Science Operations
- View records within Data Science Operations
- Access records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, AWS Admin Console, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Data Science Manager (Platform) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Data Science Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Data Science Manager (Core)

**Role ID:** `RL-DAT-60086`
**Department:** Data Science
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust HubSpot Marketing (Full Authorization Verified)
- Construct Kubernetes Production Cluster (Full Authorization Verified)
- Generate NetSuite ERP (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Configure Splunk Security Logs (Full Authorization Verified)
- Instantiate Figma Enterprise (Full Authorization Verified)
- Setup Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Instantiate Staging Environments (Full Authorization Verified)
- Access records within Data Science Operations
- Read records within Data Science Operations
- View records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Kubernetes Production Cluster, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Data Science Manager (Core) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Data Science Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Data Science Manager (Analytics)

**Role ID:** `RL-DAT-60084`
**Department:** Data Science
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Configure Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Build HubSpot Marketing (Full Authorization Verified)
- Instantiate NetSuite ERP (Full Authorization Verified)
- Manage Zendesk Support Desk (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Tweak Staging Environments (Full Authorization Verified)
- Produce Snowflake Data Warehouse (Full Authorization Verified)
- Consult records within Data Science Operations
- Consult records within Data Science Operations
- Review records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Slack Enterprise Grid, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Data Science Manager (Analytics) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Data Science Manager (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Data Science Manager (Platform)

**Role ID:** `RL-DAT-60029`
**Department:** Data Science
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Change Azure Active Directory (Full Authorization Verified)
- Adjust Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Instantiate NetSuite ERP (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Generate Salesforce CRM (Full Authorization Verified)
- Setup Snowflake Data Warehouse (Full Authorization Verified)
- Inspect records within Data Science Operations
- Access records within Data Science Operations
- Consult records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Production Database Cluster (PostgreSQL), NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Data Science Manager (Platform) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Data Science Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Lead Data Scientist

**Role ID:** `RL-DAT-50047`
**Department:** Data Science
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Create NetSuite ERP (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Change Workday HRIS (Full Authorization Verified)
- Tweak Salesforce CRM (Full Authorization Verified)
- Produce HubSpot Marketing (Full Authorization Verified)
- Construct Figma Enterprise (Full Authorization Verified)
- Consult records within Data Science Operations
- Inspect records within Data Science Operations
- Consult records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, Datadog APM, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Data Scientist needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Lead Data Scientist (Core)

**Role ID:** `RL-DAT-50068`
**Department:** Data Science
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Produce Jira System Admin (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Initialize Staging Environments (Full Authorization Verified)
- Construct Salesforce CRM (Full Authorization Verified)
- Produce Snowflake Data Warehouse (Full Authorization Verified)
- Examine records within Data Science Operations
- Examine records within Data Science Operations
- Review records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Zendesk Support Desk, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Data Scientist (Core) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Lead Data Scientist (Cloud)

**Role ID:** `RL-DAT-50014`
**Department:** Data Science
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Manage Figma Enterprise (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Setup Kubernetes Production Cluster (Full Authorization Verified)
- Produce GCP Core Infrastructure (Full Authorization Verified)
- Instantiate Workday HRIS (Full Authorization Verified)
- Produce Splunk Security Logs (Full Authorization Verified)
- Build Jira System Admin (Full Authorization Verified)
- Read records within Data Science Operations
- View records within Data Science Operations
- Audit records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, MongoDB User Data Store, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Data Scientist (Cloud) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Lead Data Scientist (Compliance)

**Role ID:** `RL-DAT-50057`
**Department:** Data Science
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Initialize Slack Enterprise Grid (Full Authorization Verified)
- Instantiate GitHub Enterprise Admin (Full Authorization Verified)
- Produce Jira System Admin (Full Authorization Verified)
- Initialize GCP Core Infrastructure (Full Authorization Verified)
- Manage Kubernetes Production Cluster (Full Authorization Verified)
- Initialize Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change MongoDB User Data Store (Full Authorization Verified)
- Read records within Data Science Operations
- Monitor records within Data Science Operations
- Access records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, GitHub Enterprise Admin, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Data Scientist (Compliance) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Lead Data Scientist (Cloud)

**Role ID:** `RL-DAT-50047`
**Department:** Data Science
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Configure MongoDB User Data Store (Full Authorization Verified)
- Initialize Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Setup AWS Admin Console (Full Authorization Verified)
- Construct Slack Enterprise Grid (Full Authorization Verified)
- Create Salesforce CRM (Full Authorization Verified)
- Modify Workday HRIS (Full Authorization Verified)
- Examine records within Data Science Operations
- Monitor records within Data Science Operations
- Inspect records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, MongoDB User Data Store, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Data Scientist (Cloud) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Data Scientist

**Role ID:** `RL-DAT-40049`
**Department:** Data Science
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Create Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Instantiate Kubernetes Production Cluster (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Generate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Access records within Data Science Operations
- Access records within Data Science Operations
- Read records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Snowflake Data Warehouse, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Data Scientist needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Data Scientist (Compliance)

**Role ID:** `RL-DAT-40091`
**Department:** Data Science
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Configure HubSpot Marketing (Full Authorization Verified)
- Create Slack Enterprise Grid (Full Authorization Verified)
- Initialize Datadog APM (Full Authorization Verified)
- Build Kubernetes Production Cluster (Full Authorization Verified)
- Build CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Examine records within Data Science Operations
- Consult records within Data Science Operations
- Review records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Slack Enterprise Grid, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Data Scientist (Compliance) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Data Scientist (Enterprise)

**Role ID:** `RL-DAT-40098`
**Department:** Data Science
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Update CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Generate Staging Environments (Full Authorization Verified)
- Build Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Setup Datadog APM (Full Authorization Verified)
- Construct AWS Admin Console (Full Authorization Verified)
- Build Figma Enterprise (Full Authorization Verified)
- Inspect records within Data Science Operations
- Consult records within Data Science Operations
- Audit records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Staging Environments, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Data Scientist (Enterprise) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Data Scientist (Analytics)

**Role ID:** `RL-DAT-40091`
**Department:** Data Science
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Configure Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Produce Slack Enterprise Grid (Full Authorization Verified)
- Adjust Workday HRIS (Full Authorization Verified)
- Produce Splunk Security Logs (Full Authorization Verified)
- Initialize Staging Environments (Full Authorization Verified)
- Setup Zendesk Support Desk (Full Authorization Verified)
- Examine records within Data Science Operations
- Access records within Data Science Operations
- Consult records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Slack Enterprise Grid, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Data Scientist (Analytics) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Data Scientist (Analytics)

**Role ID:** `RL-DAT-40027`
**Department:** Data Science
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Manage CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Alter NetSuite ERP (Full Authorization Verified)
- Create Staging Environments (Full Authorization Verified)
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Monitor records within Data Science Operations
- Access records within Data Science Operations
- Inspect records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Zendesk Support Desk, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Data Scientist (Analytics) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Data Scientist

**Role ID:** `RL-DAT-30094`
**Department:** Data Science
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Datadog APM (Full Authorization Verified)
- Consult Zendesk Support Desk (Full Authorization Verified)
- Monitor Figma Enterprise (Full Authorization Verified)
- Inspect NetSuite ERP (Full Authorization Verified)
- Inspect AWS Admin Console (Full Authorization Verified)
- Examine records within Data Science Operations
- Inspect records within Data Science Operations
- Consult records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, Zendesk Support Desk, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Scientist needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Data Scientist (Infrastructure)

**Role ID:** `RL-DAT-30022`
**Department:** Data Science
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Snowflake Data Warehouse (Full Authorization Verified)
- Examine GitHub Enterprise Admin (Full Authorization Verified)
- Read Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Read Salesforce CRM (Full Authorization Verified)
- Access Zendesk Support Desk (Full Authorization Verified)
- Examine records within Data Science Operations
- Audit records within Data Science Operations
- Monitor records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, GitHub Enterprise Admin, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Scientist (Infrastructure) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Data Scientist (Platform)

**Role ID:** `RL-DAT-30066`
**Department:** Data Science
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Zendesk Support Desk (Full Authorization Verified)
- Read Salesforce CRM (Full Authorization Verified)
- Read Splunk Security Logs (Full Authorization Verified)
- Inspect NetSuite ERP (Full Authorization Verified)
- Consult Figma Enterprise (Full Authorization Verified)
- Consult records within Data Science Operations
- Access records within Data Science Operations
- Audit records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Salesforce CRM, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Scientist (Platform) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Data Scientist (APAC Region)

**Role ID:** `RL-DAT-30043`
**Department:** Data Science
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult MongoDB User Data Store (Full Authorization Verified)
- Examine Azure Active Directory (Full Authorization Verified)
- Examine CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect GCP Core Infrastructure (Full Authorization Verified)
- Read Workday HRIS (Full Authorization Verified)
- Consult records within Data Science Operations
- Review records within Data Science Operations
- Audit records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Azure Active Directory, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Scientist (APAC Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Data Scientist (Cloud)

**Role ID:** `RL-DAT-30055`
**Department:** Data Science
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View Kubernetes Production Cluster (Full Authorization Verified)
- Audit NetSuite ERP (Full Authorization Verified)
- Inspect HubSpot Marketing (Full Authorization Verified)
- View Datadog APM (Full Authorization Verified)
- Consult GCP Core Infrastructure (Full Authorization Verified)
- Audit records within Data Science Operations
- View records within Data Science Operations
- Monitor records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, NetSuite ERP, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Scientist (Cloud) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Data Science Intern

**Role ID:** `RL-DAT-10026`
**Department:** Data Science
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Salesforce CRM (Full Authorization Verified)
- Review NetSuite ERP (Full Authorization Verified)
- View CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Access records within Data Science Operations
- Inspect records within Data Science Operations
- View records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, NetSuite ERP, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Intern needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Data Science Intern (Platform)

**Role ID:** `RL-DAT-10093`
**Department:** Data Science
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Snowflake Data Warehouse (Full Authorization Verified)
- Monitor Zendesk Support Desk (Full Authorization Verified)
- Access Salesforce CRM (Full Authorization Verified)
- Access records within Data Science Operations
- View records within Data Science Operations
- Review records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Zendesk Support Desk, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Intern (Platform) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Data Science Intern (Enterprise)

**Role ID:** `RL-DAT-10071`
**Department:** Data Science
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit HubSpot Marketing (Full Authorization Verified)
- View Splunk Security Logs (Full Authorization Verified)
- Review Staging Environments (Full Authorization Verified)
- View records within Data Science Operations
- Examine records within Data Science Operations
- View records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Splunk Security Logs, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Intern (Enterprise) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Data Science Intern (Platform)

**Role ID:** `RL-DAT-10020`
**Department:** Data Science
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor AWS Admin Console (Full Authorization Verified)
- Examine HubSpot Marketing (Full Authorization Verified)
- Read Azure Active Directory (Full Authorization Verified)
- Read records within Data Science Operations
- Consult records within Data Science Operations
- Monitor records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, HubSpot Marketing, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Intern (Platform) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Data Science Intern (Core)

**Role ID:** `RL-DAT-10057`
**Department:** Data Science
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read NetSuite ERP (Full Authorization Verified)
- View GitHub Enterprise Admin (Full Authorization Verified)
- Monitor Zendesk Support Desk (Full Authorization Verified)
- View records within Data Science Operations
- Examine records within Data Science Operations
- Read records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, GitHub Enterprise Admin, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Intern (Core) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Data Science Consultant

**Role ID:** `RL-DAT-20073`
**Department:** Data Science
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult Splunk Security Logs (Full Authorization Verified)
- Inspect MongoDB User Data Store (Full Authorization Verified)
- Audit Zendesk Support Desk (Full Authorization Verified)
- Review Staging Environments (Full Authorization Verified)
- Consult records within Data Science Operations
- Examine records within Data Science Operations
- Monitor records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, MongoDB User Data Store, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Consultant needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Data Science Consultant (Growth)

**Role ID:** `RL-DAT-20079`
**Department:** Data Science
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Slack Enterprise Grid (Full Authorization Verified)
- Inspect NetSuite ERP (Full Authorization Verified)
- Review HubSpot Marketing (Full Authorization Verified)
- Monitor Kubernetes Production Cluster (Full Authorization Verified)
- Monitor records within Data Science Operations
- Examine records within Data Science Operations
- Read records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, NetSuite ERP, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Consultant (Growth) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Data Science Consultant (Enterprise)

**Role ID:** `RL-DAT-20077`
**Department:** Data Science
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit Datadog APM (Full Authorization Verified)
- Examine GCP Core Infrastructure (Full Authorization Verified)
- Access MongoDB User Data Store (Full Authorization Verified)
- Read Zendesk Support Desk (Full Authorization Verified)
- View records within Data Science Operations
- View records within Data Science Operations
- Monitor records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, GCP Core Infrastructure, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Consultant (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Data Science Consultant (Cloud)

**Role ID:** `RL-DAT-20090`
**Department:** Data Science
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Azure Active Directory (Full Authorization Verified)
- Monitor AWS Admin Console (Full Authorization Verified)
- View GCP Core Infrastructure (Full Authorization Verified)
- Inspect NetSuite ERP (Full Authorization Verified)
- Review records within Data Science Operations
- Audit records within Data Science Operations
- Access records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, AWS Admin Console, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Consultant (Cloud) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Data Science Consultant (Infrastructure)

**Role ID:** `RL-DAT-20035`
**Department:** Data Science
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Kubernetes Production Cluster (Full Authorization Verified)
- Inspect Workday HRIS (Full Authorization Verified)
- Consult Slack Enterprise Grid (Full Authorization Verified)
- View Jira System Admin (Full Authorization Verified)
- Review records within Data Science Operations
- Access records within Data Science Operations
- Consult records within Data Science Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Data Science team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Workday HRIS, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Data Science Consultant (Infrastructure) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

