---
title: Legal RBAC Hierarchy
department: legal
role_access: employee,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## Legal Department

The Legal department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Legal Officer (CLO) / General Counsel

**Role ID:** `RL-LEG-100041`
**Department:** Legal
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Destroy MongoDB User Data Store (Full Authorization Verified)
- Drop Slack Enterprise Grid (Full Authorization Verified)
- Revoke Kubernetes Production Cluster (Full Authorization Verified)
- Revoke AWS Admin Console (Full Authorization Verified)
- Revoke Workday HRIS (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- Terminate Salesforce CRM (Full Authorization Verified)
- Erase Staging Environments (Full Authorization Verified)
- Remove GitHub Enterprise Admin (Full Authorization Verified)
- Monitor records within Legal Operations
- View records within Legal Operations
- Access records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Slack Enterprise Grid, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Legal Officer (CLO) / General Counsel needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Legal Officer (CLO) / General Counsel receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Legal Officer (CLO) / General Counsel (Cloud)

**Role ID:** `RL-LEG-100055`
**Department:** Legal
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Terminate Jira System Admin (Full Authorization Verified)
- Delete Figma Enterprise (Full Authorization Verified)
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Manage Datadog APM (Full Authorization Verified)
- Terminate Slack Enterprise Grid (Full Authorization Verified)
- Purge Workday HRIS (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Erase Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Modify Salesforce CRM (Full Authorization Verified)
- Audit records within Legal Operations
- Monitor records within Legal Operations
- Access records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing NetSuite ERP

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Jira System Admin, Figma Enterprise, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Legal Officer (CLO) / General Counsel (Cloud) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Legal Officer (CLO) / General Counsel (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Chief Legal Officer (CLO) / General Counsel (Growth)

**Role ID:** `RL-LEG-100074`
**Department:** Legal
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Modify Splunk Security Logs (Full Authorization Verified)
- Configure Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Adjust GCP Core Infrastructure (Full Authorization Verified)
- Purge CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Manage Kubernetes Production Cluster (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- Change Jira System Admin (Full Authorization Verified)
- Adjust AWS Admin Console (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Review records within Legal Operations
- Monitor records within Legal Operations
- View records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Snowflake Data Warehouse

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Splunk Security Logs, Production Database Cluster (PostgreSQL), GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Legal Officer (CLO) / General Counsel (Growth) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Legal Officer (CLO) / General Counsel (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Chief Legal Officer (CLO) / General Counsel (Cloud)

**Role ID:** `RL-LEG-100096`
**Department:** Legal
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Remove Zendesk Support Desk (Full Authorization Verified)
- Purge CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Destroy GitHub Enterprise Admin (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Erase Jira System Admin (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Erase Splunk Security Logs (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Configure Datadog APM (Full Authorization Verified)
- Change Slack Enterprise Grid (Full Authorization Verified)
- Update Kubernetes Production Cluster (Full Authorization Verified)
- Read records within Legal Operations
- Access records within Legal Operations
- Inspect records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing AWS Admin Console

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, CI/CD Pipelines (Jenkins/GitHub Actions), HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Legal Officer (CLO) / General Counsel (Cloud) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Legal Officer (CLO) / General Counsel (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Chief Legal Officer (CLO) / General Counsel (Growth)

**Role ID:** `RL-LEG-100059`
**Department:** Legal
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Destroy Figma Enterprise (Full Authorization Verified)
- Tweak Azure Active Directory (Full Authorization Verified)
- Update CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop Splunk Security Logs (Full Authorization Verified)
- Destroy Zendesk Support Desk (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Erase Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Revoke Snowflake Data Warehouse (Full Authorization Verified)
- Erase Salesforce CRM (Full Authorization Verified)
- Manage Datadog APM (Full Authorization Verified)
- Destroy GCP Core Infrastructure (Full Authorization Verified)
- View records within Legal Operations
- Examine records within Legal Operations
- Inspect records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing AWS Admin Console

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Figma Enterprise, Azure Active Directory, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Legal Officer (CLO) / General Counsel (Growth) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Legal Officer (CLO) / General Counsel (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of Legal Affairs

**Role ID:** `RL-LEG-90022`
**Department:** Legal
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Update NetSuite ERP (Full Authorization Verified)
- Destroy Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit Figma Enterprise (Full Authorization Verified)
- Erase Workday HRIS (Full Authorization Verified)
- Remove HubSpot Marketing (Full Authorization Verified)
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Purge Datadog APM (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Remove CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust GCP Core Infrastructure (Full Authorization Verified)
- Inspect records within Legal Operations
- Read records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Staging Environments

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: NetSuite ERP, Production Database Cluster (PostgreSQL), Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Legal Affairs needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Legal Affairs receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### VP of Legal Affairs (APAC Region)

**Role ID:** `RL-LEG-90099`
**Department:** Legal
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke Azure Active Directory (Full Authorization Verified)
- Revoke Jira System Admin (Full Authorization Verified)
- Delete Salesforce CRM (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Erase Zendesk Support Desk (Full Authorization Verified)
- Drop Workday HRIS (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Manage Splunk Security Logs (Full Authorization Verified)
- Purge GCP Core Infrastructure (Full Authorization Verified)
- Read records within Legal Operations
- Review records within Legal Operations
- Audit records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Azure Active Directory, Jira System Admin, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Legal Affairs (APAC Region) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Legal Affairs (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### VP of Legal Affairs (Enterprise)

**Role ID:** `RL-LEG-90077`
**Department:** Legal
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke Staging Environments (Full Authorization Verified)
- Drop Zendesk Support Desk (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Delete AWS Admin Console (Full Authorization Verified)
- Alter Workday HRIS (Full Authorization Verified)
- Change Slack Enterprise Grid (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Remove GCP Core Infrastructure (Full Authorization Verified)
- Manage GitHub Enterprise Admin (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Revoke Figma Enterprise (Full Authorization Verified)
- View records within Legal Operations
- Monitor records within Legal Operations
- Examine records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Datadog APM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, Zendesk Support Desk, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Legal Affairs (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Legal Affairs (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of Legal Affairs (Infrastructure)

**Role ID:** `RL-LEG-90017`
**Department:** Legal
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Modify Salesforce CRM (Full Authorization Verified)
- Delete Datadog APM (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Modify Jira System Admin (Full Authorization Verified)
- Configure Slack Enterprise Grid (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Drop CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Purge Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Destroy Figma Enterprise (Full Authorization Verified)
- Configure Staging Environments (Full Authorization Verified)
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- Monitor records within Legal Operations
- Audit records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Zendesk Support Desk

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Salesforce CRM, Datadog APM, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Legal Affairs (Infrastructure) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Legal Affairs (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### VP of Legal Affairs (EMEA Region)

**Role ID:** `RL-LEG-90081`
**Department:** Legal
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak Salesforce CRM (Full Authorization Verified)
- Purge Splunk Security Logs (Full Authorization Verified)
- Modify Kubernetes Production Cluster (Full Authorization Verified)
- Revoke Azure Active Directory (Full Authorization Verified)
- Destroy HubSpot Marketing (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Purge NetSuite ERP (Full Authorization Verified)
- Tweak Figma Enterprise (Full Authorization Verified)
- Drop Datadog APM (Full Authorization Verified)
- Remove Workday HRIS (Full Authorization Verified)
- Review records within Legal Operations
- Review records within Legal Operations
- Audit records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Staging Environments

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Salesforce CRM, Splunk Security Logs, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Legal Affairs (EMEA Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Legal Affairs (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Director of Legal

**Role ID:** `RL-LEG-80074`
**Department:** Legal
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Delete Datadog APM (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Purge Splunk Security Logs (Full Authorization Verified)
- Remove Kubernetes Production Cluster (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Adjust AWS Admin Console (Full Authorization Verified)
- Tweak Azure Active Directory (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Review records within Legal Operations
- Inspect records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, Production Database Cluster (PostgreSQL), Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Legal needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Legal receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Director of Legal (APAC Region)

**Role ID:** `RL-LEG-80048`
**Department:** Legal
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Datadog APM (Full Authorization Verified)
- Change AWS Admin Console (Full Authorization Verified)
- Drop Splunk Security Logs (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Change NetSuite ERP (Full Authorization Verified)
- Modify GCP Core Infrastructure (Full Authorization Verified)
- Destroy MongoDB User Data Store (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Delete CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Read records within Legal Operations
- Examine records within Legal Operations
- Review records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, AWS Admin Console, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Legal (APAC Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Legal (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Director of Legal (APAC Region)

**Role ID:** `RL-LEG-80037`
**Department:** Legal
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Drop Jira System Admin (Full Authorization Verified)
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Change NetSuite ERP (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Revoke MongoDB User Data Store (Full Authorization Verified)
- Drop Figma Enterprise (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Destroy Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Examine records within Legal Operations
- Access records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Jira System Admin, Snowflake Data Warehouse, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Legal (APAC Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Legal (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Director of Legal (Infrastructure)

**Role ID:** `RL-LEG-80068`
**Department:** Legal
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Terminate Figma Enterprise (Full Authorization Verified)
- Manage GitHub Enterprise Admin (Full Authorization Verified)
- Alter Jira System Admin (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Drop CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Edit Splunk Security Logs (Full Authorization Verified)
- Adjust Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Revoke Salesforce CRM (Full Authorization Verified)
- Modify Workday HRIS (Full Authorization Verified)
- Inspect records within Legal Operations
- Review records within Legal Operations
- Review records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Figma Enterprise, GitHub Enterprise Admin, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Legal (Infrastructure) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Legal (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Director of Legal (Growth)

**Role ID:** `RL-LEG-80029`
**Department:** Legal
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Zendesk Support Desk (Full Authorization Verified)
- Delete Snowflake Data Warehouse (Full Authorization Verified)
- Tweak AWS Admin Console (Full Authorization Verified)
- Revoke Figma Enterprise (Full Authorization Verified)
- Erase Workday HRIS (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Drop Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Configure Salesforce CRM (Full Authorization Verified)
- Terminate GitHub Enterprise Admin (Full Authorization Verified)
- Monitor records within Legal Operations
- Review records within Legal Operations
- Examine records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Legal aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Snowflake Data Warehouse, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Legal (Growth) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Legal (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Managing Counsel

**Role ID:** `RL-LEG-70098`
**Department:** Legal
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Modify MongoDB User Data Store (Full Authorization Verified)
- Produce Azure Active Directory (Full Authorization Verified)
- Generate NetSuite ERP (Full Authorization Verified)
- Construct Kubernetes Production Cluster (Full Authorization Verified)
- Instantiate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Construct Snowflake Data Warehouse (Full Authorization Verified)
- Generate Salesforce CRM (Full Authorization Verified)
- Create GCP Core Infrastructure (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Review records within Legal Operations
- Review records within Legal Operations
- Consult records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Azure Active Directory, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Managing Counsel needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Managing Counsel receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Managing Counsel (North America)

**Role ID:** `RL-LEG-70059`
**Department:** Legal
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Produce Workday HRIS (Full Authorization Verified)
- Instantiate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit Slack Enterprise Grid (Full Authorization Verified)
- Configure MongoDB User Data Store (Full Authorization Verified)
- Produce Kubernetes Production Cluster (Full Authorization Verified)
- Construct Azure Active Directory (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Instantiate GCP Core Infrastructure (Full Authorization Verified)
- Produce Staging Environments (Full Authorization Verified)
- Audit records within Legal Operations
- Monitor records within Legal Operations
- Audit records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, CI/CD Pipelines (Jenkins/GitHub Actions), Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Managing Counsel (North America) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Managing Counsel (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Managing Counsel (Growth)

**Role ID:** `RL-LEG-70090`
**Department:** Legal
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Build Staging Environments (Full Authorization Verified)
- Construct Figma Enterprise (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Instantiate GitHub Enterprise Admin (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Build GCP Core Infrastructure (Full Authorization Verified)
- Setup HubSpot Marketing (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Review records within Legal Operations
- Consult records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Figma Enterprise, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Managing Counsel (Growth) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Managing Counsel (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Managing Counsel (North America)

**Role ID:** `RL-LEG-70078`
**Department:** Legal
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Setup Snowflake Data Warehouse (Full Authorization Verified)
- Generate Splunk Security Logs (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Construct CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Generate GitHub Enterprise Admin (Full Authorization Verified)
- Edit Zendesk Support Desk (Full Authorization Verified)
- Instantiate HubSpot Marketing (Full Authorization Verified)
- Configure Azure Active Directory (Full Authorization Verified)
- Read records within Legal Operations
- Inspect records within Legal Operations
- Access records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Splunk Security Logs, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Managing Counsel (North America) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Managing Counsel (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Managing Counsel (Cloud)

**Role ID:** `RL-LEG-70011`
**Department:** Legal
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Produce Staging Environments (Full Authorization Verified)
- Instantiate Figma Enterprise (Full Authorization Verified)
- Manage Workday HRIS (Full Authorization Verified)
- Build MongoDB User Data Store (Full Authorization Verified)
- Configure Azure Active Directory (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Adjust Jira System Admin (Full Authorization Verified)
- Create Zendesk Support Desk (Full Authorization Verified)
- Read records within Legal Operations
- Review records within Legal Operations
- Inspect records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Staging Environments, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Managing Counsel (Cloud) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Managing Counsel (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Managing Counsel

**Role ID:** `RL-LEG-60012`
**Department:** Legal
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Alter Jira System Admin (Full Authorization Verified)
- Create MongoDB User Data Store (Full Authorization Verified)
- Construct CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Create AWS Admin Console (Full Authorization Verified)
- Initialize NetSuite ERP (Full Authorization Verified)
- Inspect records within Legal Operations
- Consult records within Legal Operations
- Inspect records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, MongoDB User Data Store, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Managing Counsel needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Managing Counsel receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Managing Counsel (EMEA Region)

**Role ID:** `RL-LEG-60092`
**Department:** Legal
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Produce Slack Enterprise Grid (Full Authorization Verified)
- Adjust AWS Admin Console (Full Authorization Verified)
- Edit Staging Environments (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Produce Kubernetes Production Cluster (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Configure Splunk Security Logs (Full Authorization Verified)
- Produce CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect records within Legal Operations
- Inspect records within Legal Operations
- Access records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, AWS Admin Console, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Managing Counsel (EMEA Region) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Managing Counsel (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Managing Counsel (North America)

**Role ID:** `RL-LEG-60033`
**Department:** Legal
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Edit Zendesk Support Desk (Full Authorization Verified)
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Update GitHub Enterprise Admin (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Setup Staging Environments (Full Authorization Verified)
- Change AWS Admin Console (Full Authorization Verified)
- Build Azure Active Directory (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Consult records within Legal Operations
- Read records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Slack Enterprise Grid, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Managing Counsel (North America) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Managing Counsel (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Managing Counsel (Compliance)

**Role ID:** `RL-LEG-60046`
**Department:** Legal
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Build Figma Enterprise (Full Authorization Verified)
- Create Staging Environments (Full Authorization Verified)
- Initialize Kubernetes Production Cluster (Full Authorization Verified)
- Create Zendesk Support Desk (Full Authorization Verified)
- Update Slack Enterprise Grid (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Construct Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Read records within Legal Operations
- Inspect records within Legal Operations
- Consult records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Staging Environments, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Managing Counsel (Compliance) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Managing Counsel (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Managing Counsel (Enterprise)

**Role ID:** `RL-LEG-60050`
**Department:** Legal
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Adjust CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Update Azure Active Directory (Full Authorization Verified)
- Produce Slack Enterprise Grid (Full Authorization Verified)
- Build Snowflake Data Warehouse (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Initialize Staging Environments (Full Authorization Verified)
- Examine records within Legal Operations
- Examine records within Legal Operations
- Access records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, CI/CD Pipelines (Jenkins/GitHub Actions), GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Managing Counsel (Enterprise) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Managing Counsel (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Lead Counsel

**Role ID:** `RL-LEG-50073`
**Department:** Legal
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Modify Kubernetes Production Cluster (Full Authorization Verified)
- Produce Staging Environments (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Instantiate Figma Enterprise (Full Authorization Verified)
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Create Azure Active Directory (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Review records within Legal Operations
- Audit records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Staging Environments, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Counsel needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Lead Counsel (North America)

**Role ID:** `RL-LEG-50063`
**Department:** Legal
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Initialize GCP Core Infrastructure (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Adjust Workday HRIS (Full Authorization Verified)
- Modify Jira System Admin (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Generate Slack Enterprise Grid (Full Authorization Verified)
- Consult records within Legal Operations
- Review records within Legal Operations
- Access records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, GCP Core Infrastructure, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Counsel (North America) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Lead Counsel (North America)

**Role ID:** `RL-LEG-50081`
**Department:** Legal
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Alter Salesforce CRM (Full Authorization Verified)
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Change GCP Core Infrastructure (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Tweak Datadog APM (Full Authorization Verified)
- Generate HubSpot Marketing (Full Authorization Verified)
- Access records within Legal Operations
- Access records within Legal Operations
- Access records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, CI/CD Pipelines (Jenkins/GitHub Actions), Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Counsel (North America) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Lead Counsel (Cloud)

**Role ID:** `RL-LEG-50051`
**Department:** Legal
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Construct MongoDB User Data Store (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Modify AWS Admin Console (Full Authorization Verified)
- Generate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Produce Salesforce CRM (Full Authorization Verified)
- Update Slack Enterprise Grid (Full Authorization Verified)
- Examine records within Legal Operations
- View records within Legal Operations
- Monitor records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, MongoDB User Data Store, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Counsel (Cloud) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Lead Counsel (Enterprise)

**Role ID:** `RL-LEG-50028`
**Department:** Legal
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Build Staging Environments (Full Authorization Verified)
- Edit Snowflake Data Warehouse (Full Authorization Verified)
- Produce Kubernetes Production Cluster (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Initialize GitHub Enterprise Admin (Full Authorization Verified)
- Generate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Read records within Legal Operations
- Consult records within Legal Operations
- Inspect records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Staging Environments, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Counsel (Enterprise) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Corporate Counsel

**Role ID:** `RL-LEG-40014`
**Department:** Legal
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Alter Figma Enterprise (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Construct CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Instantiate Staging Environments (Full Authorization Verified)
- Create Kubernetes Production Cluster (Full Authorization Verified)
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Monitor records within Legal Operations
- Consult records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Datadog APM, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Corporate Counsel needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Corporate Counsel (Enterprise)

**Role ID:** `RL-LEG-40025`
**Department:** Legal
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Change Salesforce CRM (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Produce Azure Active Directory (Full Authorization Verified)
- Generate HubSpot Marketing (Full Authorization Verified)
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Create Slack Enterprise Grid (Full Authorization Verified)
- Monitor records within Legal Operations
- View records within Legal Operations
- Monitor records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, Snowflake Data Warehouse, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Corporate Counsel (Enterprise) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Corporate Counsel (Growth)

**Role ID:** `RL-LEG-40066`
**Department:** Legal
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Tweak HubSpot Marketing (Full Authorization Verified)
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Initialize Slack Enterprise Grid (Full Authorization Verified)
- Manage CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Modify Jira System Admin (Full Authorization Verified)
- Change NetSuite ERP (Full Authorization Verified)
- Access records within Legal Operations
- Examine records within Legal Operations
- Examine records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Production Database Cluster (PostgreSQL), Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Corporate Counsel (Growth) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Corporate Counsel (North America)

**Role ID:** `RL-LEG-40024`
**Department:** Legal
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Manage Zendesk Support Desk (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Construct CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Build Jira System Admin (Full Authorization Verified)
- Adjust Splunk Security Logs (Full Authorization Verified)
- Review records within Legal Operations
- Read records within Legal Operations
- Review records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Kubernetes Production Cluster, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Corporate Counsel (North America) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Corporate Counsel (EMEA Region)

**Role ID:** `RL-LEG-40043`
**Department:** Legal
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Setup Staging Environments (Full Authorization Verified)
- Generate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Initialize Workday HRIS (Full Authorization Verified)
- Instantiate MongoDB User Data Store (Full Authorization Verified)
- Initialize Jira System Admin (Full Authorization Verified)
- Construct Salesforce CRM (Full Authorization Verified)
- Read records within Legal Operations
- Audit records within Legal Operations
- Examine records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Production Database Cluster (PostgreSQL), Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Corporate Counsel (EMEA Region) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Corporate Counsel

**Role ID:** `RL-LEG-30038`
**Department:** Legal
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit Kubernetes Production Cluster (Full Authorization Verified)
- Examine Figma Enterprise (Full Authorization Verified)
- Audit Workday HRIS (Full Authorization Verified)
- Examine GitHub Enterprise Admin (Full Authorization Verified)
- Consult Splunk Security Logs (Full Authorization Verified)
- Inspect records within Legal Operations
- Consult records within Legal Operations
- Inspect records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Figma Enterprise, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Corporate Counsel needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Corporate Counsel (APAC Region)

**Role ID:** `RL-LEG-30085`
**Department:** Legal
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Slack Enterprise Grid (Full Authorization Verified)
- Examine NetSuite ERP (Full Authorization Verified)
- Read Datadog APM (Full Authorization Verified)
- Audit Jira System Admin (Full Authorization Verified)
- Read Kubernetes Production Cluster (Full Authorization Verified)
- Review records within Legal Operations
- Consult records within Legal Operations
- Audit records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, NetSuite ERP, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Corporate Counsel (APAC Region) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Corporate Counsel (Core)

**Role ID:** `RL-LEG-30023`
**Department:** Legal
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Inspect Datadog APM (Full Authorization Verified)
- Inspect Jira System Admin (Full Authorization Verified)
- View Zendesk Support Desk (Full Authorization Verified)
- Audit AWS Admin Console (Full Authorization Verified)
- Review records within Legal Operations
- Audit records within Legal Operations
- Access records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Datadog APM, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Corporate Counsel (Core) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Corporate Counsel (Growth)

**Role ID:** `RL-LEG-30074`
**Department:** Legal
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Workday HRIS (Full Authorization Verified)
- Audit Azure Active Directory (Full Authorization Verified)
- Inspect NetSuite ERP (Full Authorization Verified)
- Access Salesforce CRM (Full Authorization Verified)
- Review Splunk Security Logs (Full Authorization Verified)
- Monitor records within Legal Operations
- Audit records within Legal Operations
- Examine records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Azure Active Directory, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Corporate Counsel (Growth) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Corporate Counsel (Cloud)

**Role ID:** `RL-LEG-30087`
**Department:** Legal
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Zendesk Support Desk (Full Authorization Verified)
- View Kubernetes Production Cluster (Full Authorization Verified)
- Examine Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Monitor NetSuite ERP (Full Authorization Verified)
- View Snowflake Data Warehouse (Full Authorization Verified)
- Monitor records within Legal Operations
- Inspect records within Legal Operations
- View records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Kubernetes Production Cluster, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Corporate Counsel (Cloud) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Legal Intern

**Role ID:** `RL-LEG-10074`
**Department:** Legal
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Examine Salesforce CRM (Full Authorization Verified)
- Monitor NetSuite ERP (Full Authorization Verified)
- Read records within Legal Operations
- Read records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Salesforce CRM, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Legal Intern needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Legal Intern (Core)

**Role ID:** `RL-LEG-10042`
**Department:** Legal
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Datadog APM (Full Authorization Verified)
- Audit HubSpot Marketing (Full Authorization Verified)
- Review Azure Active Directory (Full Authorization Verified)
- Inspect records within Legal Operations
- Access records within Legal Operations
- Monitor records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, HubSpot Marketing, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Legal Intern (Core) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Legal Intern (North America)

**Role ID:** `RL-LEG-10083`
**Department:** Legal
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Snowflake Data Warehouse (Full Authorization Verified)
- Examine GCP Core Infrastructure (Full Authorization Verified)
- Read CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Review records within Legal Operations
- Examine records within Legal Operations
- Consult records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, GCP Core Infrastructure, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Legal Intern (North America) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Legal Intern (APAC Region)

**Role ID:** `RL-LEG-10012`
**Department:** Legal
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Snowflake Data Warehouse (Full Authorization Verified)
- Inspect Salesforce CRM (Full Authorization Verified)
- Read AWS Admin Console (Full Authorization Verified)
- Consult records within Legal Operations
- Audit records within Legal Operations
- View records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Salesforce CRM, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Legal Intern (APAC Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Legal Intern (Analytics)

**Role ID:** `RL-LEG-10091`
**Department:** Legal
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Workday HRIS (Full Authorization Verified)
- Inspect Azure Active Directory (Full Authorization Verified)
- Examine GitHub Enterprise Admin (Full Authorization Verified)
- Inspect records within Legal Operations
- Examine records within Legal Operations
- Monitor records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Azure Active Directory, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Legal Intern (Analytics) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Contract Attorney

**Role ID:** `RL-LEG-20027`
**Department:** Legal
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect NetSuite ERP (Full Authorization Verified)
- Consult Azure Active Directory (Full Authorization Verified)
- Monitor Slack Enterprise Grid (Full Authorization Verified)
- Access GitHub Enterprise Admin (Full Authorization Verified)
- Audit records within Legal Operations
- Audit records within Legal Operations
- Consult records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, Azure Active Directory, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Attorney needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Contract Attorney (Compliance)

**Role ID:** `RL-LEG-20070`
**Department:** Legal
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review NetSuite ERP (Full Authorization Verified)
- View AWS Admin Console (Full Authorization Verified)
- Monitor Salesforce CRM (Full Authorization Verified)
- Access GitHub Enterprise Admin (Full Authorization Verified)
- Audit records within Legal Operations
- View records within Legal Operations
- Monitor records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, AWS Admin Console, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Attorney (Compliance) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Contract Attorney (Enterprise)

**Role ID:** `RL-LEG-20099`
**Department:** Legal
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View GitHub Enterprise Admin (Full Authorization Verified)
- Review AWS Admin Console (Full Authorization Verified)
- Inspect Staging Environments (Full Authorization Verified)
- Consult HubSpot Marketing (Full Authorization Verified)
- Read records within Legal Operations
- Inspect records within Legal Operations
- Read records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, AWS Admin Console, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Attorney (Enterprise) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Contract Attorney (Cloud)

**Role ID:** `RL-LEG-20030`
**Department:** Legal
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Slack Enterprise Grid (Full Authorization Verified)
- Monitor CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Consult Figma Enterprise (Full Authorization Verified)
- Consult Azure Active Directory (Full Authorization Verified)
- Audit records within Legal Operations
- Review records within Legal Operations
- Review records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, CI/CD Pipelines (Jenkins/GitHub Actions), Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Attorney (Cloud) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Contract Attorney (North America)

**Role ID:** `RL-LEG-20061`
**Department:** Legal
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect GCP Core Infrastructure (Full Authorization Verified)
- Inspect Azure Active Directory (Full Authorization Verified)
- Audit Datadog APM (Full Authorization Verified)
- Consult records within Legal Operations
- Consult records within Legal Operations
- Review records within Legal Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Legal team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), GCP Core Infrastructure, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Attorney (North America) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

