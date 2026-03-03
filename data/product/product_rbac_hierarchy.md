---
title: Product RBAC Hierarchy
department: product
role_access: engineering,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## Product Department

The Product department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Product Officer (CPO)

**Role ID:** `RL-PRO-100059`
**Department:** Product
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Purge Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Tweak MongoDB User Data Store (Full Authorization Verified)
- Terminate Zendesk Support Desk (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Erase Staging Environments (Full Authorization Verified)
- Drop Datadog APM (Full Authorization Verified)
- Remove Slack Enterprise Grid (Full Authorization Verified)
- Destroy Kubernetes Production Cluster (Full Authorization Verified)
- Update Azure Active Directory (Full Authorization Verified)
- Destroy GCP Core Infrastructure (Full Authorization Verified)
- Remove HubSpot Marketing (Full Authorization Verified)
- Revoke Workday HRIS (Full Authorization Verified)
- Audit records within Product Operations
- View records within Product Operations
- Consult records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing GitHub Enterprise Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), MongoDB User Data Store, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Product Officer (CPO) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Product Officer (CPO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Chief Product Officer (CPO) (Cloud)

**Role ID:** `RL-PRO-100016`
**Department:** Product
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke Staging Environments (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Delete AWS Admin Console (Full Authorization Verified)
- Drop Jira System Admin (Full Authorization Verified)
- Adjust Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Drop Figma Enterprise (Full Authorization Verified)
- Revoke Datadog APM (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Purge GCP Core Infrastructure (Full Authorization Verified)
- Delete Splunk Security Logs (Full Authorization Verified)
- Access records within Product Operations
- Examine records within Product Operations
- Examine records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing MongoDB User Data Store

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, HubSpot Marketing, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Product Officer (CPO) (Cloud) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Product Officer (CPO) (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Chief Product Officer (CPO) (Analytics)

**Role ID:** `RL-PRO-100024`
**Department:** Product
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Manage Datadog APM (Full Authorization Verified)
- Alter Zendesk Support Desk (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Delete NetSuite ERP (Full Authorization Verified)
- Purge Figma Enterprise (Full Authorization Verified)
- Revoke GCP Core Infrastructure (Full Authorization Verified)
- Modify AWS Admin Console (Full Authorization Verified)
- Manage CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit Kubernetes Production Cluster (Full Authorization Verified)
- Adjust Jira System Admin (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Erase MongoDB User Data Store (Full Authorization Verified)
- Access records within Product Operations
- Consult records within Product Operations
- Read records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing GitHub Enterprise Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, Zendesk Support Desk, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Product Officer (CPO) (Analytics) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Product Officer (CPO) (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Chief Product Officer (CPO) (Compliance)

**Role ID:** `RL-PRO-100021`
**Department:** Product
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Alter Splunk Security Logs (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Edit Azure Active Directory (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Modify HubSpot Marketing (Full Authorization Verified)
- Terminate Figma Enterprise (Full Authorization Verified)
- Adjust Staging Environments (Full Authorization Verified)
- Purge GCP Core Infrastructure (Full Authorization Verified)
- Purge Datadog APM (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Delete Kubernetes Production Cluster (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- View records within Product Operations
- View records within Product Operations
- Consult records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Snowflake Data Warehouse

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Splunk Security Logs, Zendesk Support Desk, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Product Officer (CPO) (Compliance) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Product Officer (CPO) (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Chief Product Officer (CPO) (Growth)

**Role ID:** `RL-PRO-100040`
**Department:** Product
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Delete Jira System Admin (Full Authorization Verified)
- Tweak Workday HRIS (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Drop HubSpot Marketing (Full Authorization Verified)
- Update Splunk Security Logs (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Update GitHub Enterprise Admin (Full Authorization Verified)
- Edit Azure Active Directory (Full Authorization Verified)
- Erase CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Update Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Terminate Snowflake Data Warehouse (Full Authorization Verified)
- View records within Product Operations
- Examine records within Product Operations
- Review records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Figma Enterprise

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Jira System Admin, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Product Officer (CPO) (Growth) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Product Officer (CPO) (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### VP of Product

**Role ID:** `RL-PRO-90058`
**Department:** Product
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Delete Kubernetes Production Cluster (Full Authorization Verified)
- Remove Jira System Admin (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Delete HubSpot Marketing (Full Authorization Verified)
- Remove Snowflake Data Warehouse (Full Authorization Verified)
- Erase GCP Core Infrastructure (Full Authorization Verified)
- Modify Figma Enterprise (Full Authorization Verified)
- Change MongoDB User Data Store (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Tweak Salesforce CRM (Full Authorization Verified)
- Consult records within Product Operations
- Review records within Product Operations
- Inspect records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Zendesk Support Desk

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Jira System Admin, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Product needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Product receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### VP of Product (Enterprise)

**Role ID:** `RL-PRO-90063`
**Department:** Product
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Update Zendesk Support Desk (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Delete Splunk Security Logs (Full Authorization Verified)
- Drop AWS Admin Console (Full Authorization Verified)
- Update Azure Active Directory (Full Authorization Verified)
- Update Staging Environments (Full Authorization Verified)
- Manage Workday HRIS (Full Authorization Verified)
- Drop Snowflake Data Warehouse (Full Authorization Verified)
- Update Figma Enterprise (Full Authorization Verified)
- Audit records within Product Operations
- Consult records within Product Operations
- Audit records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing NetSuite ERP

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Zendesk Support Desk, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Product (Enterprise) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Product (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### VP of Product (Analytics)

**Role ID:** `RL-PRO-90010`
**Department:** Product
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Update Splunk Security Logs (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Terminate Figma Enterprise (Full Authorization Verified)
- Delete Slack Enterprise Grid (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Remove Kubernetes Production Cluster (Full Authorization Verified)
- Destroy Workday HRIS (Full Authorization Verified)
- Drop Salesforce CRM (Full Authorization Verified)
- Terminate AWS Admin Console (Full Authorization Verified)
- Read records within Product Operations
- Consult records within Product Operations
- Read records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Splunk Security Logs, CI/CD Pipelines (Jenkins/GitHub Actions), MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Product (Analytics) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Product (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### VP of Product (Enterprise)

**Role ID:** `RL-PRO-90069`
**Department:** Product
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Purge GitHub Enterprise Admin (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Destroy MongoDB User Data Store (Full Authorization Verified)
- Delete Staging Environments (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- Update Kubernetes Production Cluster (Full Authorization Verified)
- Tweak AWS Admin Console (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Erase Salesforce CRM (Full Authorization Verified)
- Erase Splunk Security Logs (Full Authorization Verified)
- Inspect records within Product Operations
- Review records within Product Operations
- View records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Slack Enterprise Grid

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Figma Enterprise, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Product (Enterprise) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Product (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### VP of Product (Core)

**Role ID:** `RL-PRO-90096`
**Department:** Product
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Alter Datadog APM (Full Authorization Verified)
- Remove MongoDB User Data Store (Full Authorization Verified)
- Change Slack Enterprise Grid (Full Authorization Verified)
- Remove HubSpot Marketing (Full Authorization Verified)
- Terminate AWS Admin Console (Full Authorization Verified)
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- Terminate Jira System Admin (Full Authorization Verified)
- Delete Salesforce CRM (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Drop Azure Active Directory (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Audit records within Product Operations
- View records within Product Operations
- View records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Splunk Security Logs

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, MongoDB User Data Store, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Product (Core) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Product (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Product Director

**Role ID:** `RL-PRO-80052`
**Department:** Product
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Terminate GitHub Enterprise Admin (Full Authorization Verified)
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Purge Figma Enterprise (Full Authorization Verified)
- Update AWS Admin Console (Full Authorization Verified)
- Update Staging Environments (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Destroy Jira System Admin (Full Authorization Verified)
- Drop Workday HRIS (Full Authorization Verified)
- Delete NetSuite ERP (Full Authorization Verified)
- Destroy Splunk Security Logs (Full Authorization Verified)
- Consult records within Product Operations
- Review records within Product Operations
- Access records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Production Database Cluster (PostgreSQL), Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Product Director needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Product Director receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Product Director (Infrastructure)

**Role ID:** `RL-PRO-80090`
**Department:** Product
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Terminate Staging Environments (Full Authorization Verified)
- Remove Salesforce CRM (Full Authorization Verified)
- Manage Jira System Admin (Full Authorization Verified)
- Configure Slack Enterprise Grid (Full Authorization Verified)
- Adjust GCP Core Infrastructure (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Destroy AWS Admin Console (Full Authorization Verified)
- Erase Datadog APM (Full Authorization Verified)
- Examine records within Product Operations
- Examine records within Product Operations
- Audit records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, MongoDB User Data Store, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Product Director (Infrastructure) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Product Director (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Product Director (Growth)

**Role ID:** `RL-PRO-80016`
**Department:** Product
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Destroy HubSpot Marketing (Full Authorization Verified)
- Remove Kubernetes Production Cluster (Full Authorization Verified)
- Change MongoDB User Data Store (Full Authorization Verified)
- Erase Azure Active Directory (Full Authorization Verified)
- Delete Slack Enterprise Grid (Full Authorization Verified)
- Terminate Salesforce CRM (Full Authorization Verified)
- Modify Workday HRIS (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- Purge Datadog APM (Full Authorization Verified)
- Delete Splunk Security Logs (Full Authorization Verified)
- Inspect records within Product Operations
- Read records within Product Operations
- Access records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: HubSpot Marketing, Kubernetes Production Cluster, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Product Director (Growth) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Product Director (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Product Director (Analytics)

**Role ID:** `RL-PRO-80023`
**Department:** Product
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Drop Datadog APM (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Erase Kubernetes Production Cluster (Full Authorization Verified)
- Revoke Staging Environments (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Change Figma Enterprise (Full Authorization Verified)
- Modify Workday HRIS (Full Authorization Verified)
- Drop Jira System Admin (Full Authorization Verified)
- Terminate Azure Active Directory (Full Authorization Verified)
- Examine records within Product Operations
- Audit records within Product Operations
- Review records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, HubSpot Marketing, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Product Director (Analytics) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Product Director (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Product Director (Compliance)

**Role ID:** `RL-PRO-80019`
**Department:** Product
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Remove GitHub Enterprise Admin (Full Authorization Verified)
- Destroy CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Purge Azure Active Directory (Full Authorization Verified)
- Drop Staging Environments (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Edit Splunk Security Logs (Full Authorization Verified)
- Revoke GCP Core Infrastructure (Full Authorization Verified)
- Adjust Figma Enterprise (Full Authorization Verified)
- Remove Slack Enterprise Grid (Full Authorization Verified)
- Consult records within Product Operations
- Read records within Product Operations
- Consult records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Product aggregate data.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, CI/CD Pipelines (Jenkins/GitHub Actions), Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Product Director (Compliance) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Product Director (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Group Product Manager

**Role ID:** `RL-PRO-70041`
**Department:** Product
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Construct Slack Enterprise Grid (Full Authorization Verified)
- Construct Kubernetes Production Cluster (Full Authorization Verified)
- Update Splunk Security Logs (Full Authorization Verified)
- Update GitHub Enterprise Admin (Full Authorization Verified)
- Update AWS Admin Console (Full Authorization Verified)
- Adjust Staging Environments (Full Authorization Verified)
- Build Figma Enterprise (Full Authorization Verified)
- Access records within Product Operations
- Inspect records within Product Operations
- Read records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Datadog APM, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Group Product Manager needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Group Product Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Group Product Manager (Platform)

**Role ID:** `RL-PRO-70080`
**Department:** Product
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Generate GCP Core Infrastructure (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- Build Salesforce CRM (Full Authorization Verified)
- Create Datadog APM (Full Authorization Verified)
- Alter AWS Admin Console (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Initialize GitHub Enterprise Admin (Full Authorization Verified)
- Audit records within Product Operations
- Examine records within Product Operations
- Examine records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Splunk Security Logs, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Group Product Manager (Platform) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Group Product Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Group Product Manager (North America)

**Role ID:** `RL-PRO-70026`
**Department:** Product
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Produce HubSpot Marketing (Full Authorization Verified)
- Instantiate GCP Core Infrastructure (Full Authorization Verified)
- Setup Datadog APM (Full Authorization Verified)
- Adjust Zendesk Support Desk (Full Authorization Verified)
- Create Salesforce CRM (Full Authorization Verified)
- Generate NetSuite ERP (Full Authorization Verified)
- Construct Splunk Security Logs (Full Authorization Verified)
- Instantiate Staging Environments (Full Authorization Verified)
- Instantiate Snowflake Data Warehouse (Full Authorization Verified)
- Read records within Product Operations
- Examine records within Product Operations
- Examine records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, GCP Core Infrastructure, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Group Product Manager (North America) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Group Product Manager (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Group Product Manager (Platform)

**Role ID:** `RL-PRO-70013`
**Department:** Product
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Setup GitHub Enterprise Admin (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Construct MongoDB User Data Store (Full Authorization Verified)
- Instantiate Workday HRIS (Full Authorization Verified)
- Alter NetSuite ERP (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Adjust CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Initialize Snowflake Data Warehouse (Full Authorization Verified)
- Audit records within Product Operations
- Inspect records within Product Operations
- Audit records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Production Database Cluster (PostgreSQL), Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Group Product Manager (Platform) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Group Product Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Group Product Manager (Growth)

**Role ID:** `RL-PRO-70021`
**Department:** Product
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Manage Figma Enterprise (Full Authorization Verified)
- Instantiate Zendesk Support Desk (Full Authorization Verified)
- Create Workday HRIS (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Setup Slack Enterprise Grid (Full Authorization Verified)
- Setup GCP Core Infrastructure (Full Authorization Verified)
- Construct HubSpot Marketing (Full Authorization Verified)
- Update Kubernetes Production Cluster (Full Authorization Verified)
- Read records within Product Operations
- Inspect records within Product Operations
- Review records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Zendesk Support Desk, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Group Product Manager (Growth) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Group Product Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Group Product Manager

**Role ID:** `RL-PRO-60045`
**Department:** Product
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Setup Kubernetes Production Cluster (Full Authorization Verified)
- Produce NetSuite ERP (Full Authorization Verified)
- Edit Snowflake Data Warehouse (Full Authorization Verified)
- Build Salesforce CRM (Full Authorization Verified)
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Produce HubSpot Marketing (Full Authorization Verified)
- Construct GitHub Enterprise Admin (Full Authorization Verified)
- Review records within Product Operations
- Examine records within Product Operations
- Consult records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, NetSuite ERP, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Group Product Manager needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Group Product Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Group Product Manager (Compliance)

**Role ID:** `RL-PRO-60088`
**Department:** Product
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Instantiate Slack Enterprise Grid (Full Authorization Verified)
- Construct GitHub Enterprise Admin (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Change AWS Admin Console (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Monitor records within Product Operations
- Monitor records within Product Operations
- Access records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Slack Enterprise Grid, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Group Product Manager (Compliance) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Group Product Manager (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Group Product Manager (APAC Region)

**Role ID:** `RL-PRO-60016`
**Department:** Product
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Setup Datadog APM (Full Authorization Verified)
- Adjust Staging Environments (Full Authorization Verified)
- Tweak Salesforce CRM (Full Authorization Verified)
- Initialize MongoDB User Data Store (Full Authorization Verified)
- Create Snowflake Data Warehouse (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Generate Jira System Admin (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Review records within Product Operations
- Inspect records within Product Operations
- Read records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, Staging Environments, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Group Product Manager (APAC Region) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Group Product Manager (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Group Product Manager (APAC Region)

**Role ID:** `RL-PRO-60043`
**Department:** Product
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Produce Zendesk Support Desk (Full Authorization Verified)
- Update Slack Enterprise Grid (Full Authorization Verified)
- Instantiate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Initialize Kubernetes Production Cluster (Full Authorization Verified)
- Initialize Salesforce CRM (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Construct HubSpot Marketing (Full Authorization Verified)
- Audit records within Product Operations
- Inspect records within Product Operations
- Read records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Slack Enterprise Grid, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Group Product Manager (APAC Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Group Product Manager (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Group Product Manager (Platform)

**Role ID:** `RL-PRO-60081`
**Department:** Product
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Change Figma Enterprise (Full Authorization Verified)
- Build Datadog APM (Full Authorization Verified)
- Instantiate Kubernetes Production Cluster (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Modify AWS Admin Console (Full Authorization Verified)
- Produce NetSuite ERP (Full Authorization Verified)
- Create Snowflake Data Warehouse (Full Authorization Verified)
- Build Splunk Security Logs (Full Authorization Verified)
- Monitor records within Product Operations
- Examine records within Product Operations
- Inspect records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Datadog APM, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Group Product Manager (Platform) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Group Product Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Lead Product Manager

**Role ID:** `RL-PRO-50045`
**Department:** Product
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Create MongoDB User Data Store (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Configure Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Modify GitHub Enterprise Admin (Full Authorization Verified)
- Instantiate Figma Enterprise (Full Authorization Verified)
- Initialize Splunk Security Logs (Full Authorization Verified)
- Alter Jira System Admin (Full Authorization Verified)
- Monitor records within Product Operations
- Monitor records within Product Operations
- Inspect records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Datadog APM, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Product Manager needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Lead Product Manager (North America)

**Role ID:** `RL-PRO-50026`
**Department:** Product
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Update Workday HRIS (Full Authorization Verified)
- Construct Jira System Admin (Full Authorization Verified)
- Create Kubernetes Production Cluster (Full Authorization Verified)
- Update Datadog APM (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Setup Figma Enterprise (Full Authorization Verified)
- Inspect records within Product Operations
- Read records within Product Operations
- Consult records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Jira System Admin, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Product Manager (North America) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Lead Product Manager (EMEA Region)

**Role ID:** `RL-PRO-50036`
**Department:** Product
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Tweak Figma Enterprise (Full Authorization Verified)
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Setup NetSuite ERP (Full Authorization Verified)
- Adjust Zendesk Support Desk (Full Authorization Verified)
- Produce AWS Admin Console (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Update Datadog APM (Full Authorization Verified)
- Review records within Product Operations
- Monitor records within Product Operations
- Read records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Production Database Cluster (PostgreSQL), NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Product Manager (EMEA Region) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Lead Product Manager (Infrastructure)

**Role ID:** `RL-PRO-50051`
**Department:** Product
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Tweak AWS Admin Console (Full Authorization Verified)
- Build Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Build Zendesk Support Desk (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Produce GCP Core Infrastructure (Full Authorization Verified)
- Access records within Product Operations
- Inspect records within Product Operations
- Read records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Production Database Cluster (PostgreSQL), Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Product Manager (Infrastructure) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Lead Product Manager (North America)

**Role ID:** `RL-PRO-50082`
**Department:** Product
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Setup Splunk Security Logs (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Edit Staging Environments (Full Authorization Verified)
- Construct Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Configure Azure Active Directory (Full Authorization Verified)
- Create AWS Admin Console (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Audit records within Product Operations
- Access records within Product Operations
- Consult records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, Salesforce CRM, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Lead Product Manager (North America) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Product Manager

**Role ID:** `RL-PRO-40029`
**Department:** Product
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Produce Snowflake Data Warehouse (Full Authorization Verified)
- Create Staging Environments (Full Authorization Verified)
- Produce Splunk Security Logs (Full Authorization Verified)
- Create Workday HRIS (Full Authorization Verified)
- Update Figma Enterprise (Full Authorization Verified)
- Construct CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Review records within Product Operations
- View records within Product Operations
- View records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Staging Environments, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Product Manager needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Product Manager (Cloud)

**Role ID:** `RL-PRO-40016`
**Department:** Product
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Tweak MongoDB User Data Store (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Setup Figma Enterprise (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Manage GitHub Enterprise Admin (Full Authorization Verified)
- Manage Workday HRIS (Full Authorization Verified)
- Consult records within Product Operations
- Read records within Product Operations
- View records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Splunk Security Logs, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Product Manager (Cloud) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Product Manager (Compliance)

**Role ID:** `RL-PRO-40034`
**Department:** Product
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Initialize GCP Core Infrastructure (Full Authorization Verified)
- Construct Zendesk Support Desk (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Tweak AWS Admin Console (Full Authorization Verified)
- Initialize Salesforce CRM (Full Authorization Verified)
- Monitor records within Product Operations
- Inspect records within Product Operations
- View records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Zendesk Support Desk, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Product Manager (Compliance) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Product Manager (North America)

**Role ID:** `RL-PRO-40018`
**Department:** Product
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Alter Figma Enterprise (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Generate Kubernetes Production Cluster (Full Authorization Verified)
- Produce Splunk Security Logs (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Initialize Slack Enterprise Grid (Full Authorization Verified)
- Read records within Product Operations
- View records within Product Operations
- Audit records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Staging Environments, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Product Manager (North America) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Product Manager (Infrastructure)

**Role ID:** `RL-PRO-40085`
**Department:** Product
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Modify Kubernetes Production Cluster (Full Authorization Verified)
- Construct Datadog APM (Full Authorization Verified)
- Alter Salesforce CRM (Full Authorization Verified)
- Instantiate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Tweak GitHub Enterprise Admin (Full Authorization Verified)
- Produce Zendesk Support Desk (Full Authorization Verified)
- Review records within Product Operations
- Consult records within Product Operations
- Access records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Datadog APM, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Product Manager (Infrastructure) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Product Manager

**Role ID:** `RL-PRO-30071`
**Department:** Product
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit AWS Admin Console (Full Authorization Verified)
- Inspect Jira System Admin (Full Authorization Verified)
- Access Figma Enterprise (Full Authorization Verified)
- Consult Snowflake Data Warehouse (Full Authorization Verified)
- Examine Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Consult records within Product Operations
- Audit records within Product Operations
- Access records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Jira System Admin, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Manager needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Product Manager (Analytics)

**Role ID:** `RL-PRO-30035`
**Department:** Product
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine GCP Core Infrastructure (Full Authorization Verified)
- Audit Splunk Security Logs (Full Authorization Verified)
- Audit Kubernetes Production Cluster (Full Authorization Verified)
- Review AWS Admin Console (Full Authorization Verified)
- View MongoDB User Data Store (Full Authorization Verified)
- Access records within Product Operations
- Access records within Product Operations
- Examine records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Splunk Security Logs, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Manager (Analytics) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Product Manager (Infrastructure)

**Role ID:** `RL-PRO-30034`
**Department:** Product
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View Salesforce CRM (Full Authorization Verified)
- View Slack Enterprise Grid (Full Authorization Verified)
- View Kubernetes Production Cluster (Full Authorization Verified)
- View Azure Active Directory (Full Authorization Verified)
- Examine records within Product Operations
- Inspect records within Product Operations
- Monitor records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Salesforce CRM, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Manager (Infrastructure) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Product Manager (Analytics)

**Role ID:** `RL-PRO-30075`
**Department:** Product
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Zendesk Support Desk (Full Authorization Verified)
- Read CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- View Staging Environments (Full Authorization Verified)
- Access Workday HRIS (Full Authorization Verified)
- Read GitHub Enterprise Admin (Full Authorization Verified)
- View records within Product Operations
- Access records within Product Operations
- Monitor records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, CI/CD Pipelines (Jenkins/GitHub Actions), Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Manager (Analytics) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Product Manager (Platform)

**Role ID:** `RL-PRO-30010`
**Department:** Product
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Salesforce CRM (Full Authorization Verified)
- Review MongoDB User Data Store (Full Authorization Verified)
- Review Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View GitHub Enterprise Admin (Full Authorization Verified)
- Review Staging Environments (Full Authorization Verified)
- Consult records within Product Operations
- Audit records within Product Operations
- Monitor records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, MongoDB User Data Store, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Manager (Platform) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Product Intern

**Role ID:** `RL-PRO-10016`
**Department:** Product
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Splunk Security Logs (Full Authorization Verified)
- Access MongoDB User Data Store (Full Authorization Verified)
- View Zendesk Support Desk (Full Authorization Verified)
- View records within Product Operations
- Audit records within Product Operations
- Review records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, MongoDB User Data Store, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Intern needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Product Intern (Growth)

**Role ID:** `RL-PRO-10016`
**Department:** Product
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult AWS Admin Console (Full Authorization Verified)
- Read Workday HRIS (Full Authorization Verified)
- Access CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Consult records within Product Operations
- View records within Product Operations
- Audit records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Workday HRIS, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Intern (Growth) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Product Intern (Cloud)

**Role ID:** `RL-PRO-10061`
**Department:** Product
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult Azure Active Directory (Full Authorization Verified)
- View MongoDB User Data Store (Full Authorization Verified)
- Consult Figma Enterprise (Full Authorization Verified)
- Read records within Product Operations
- Audit records within Product Operations
- Access records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, MongoDB User Data Store, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Intern (Cloud) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Product Intern (Compliance)

**Role ID:** `RL-PRO-10044`
**Department:** Product
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult Azure Active Directory (Full Authorization Verified)
- Access NetSuite ERP (Full Authorization Verified)
- Consult CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Read records within Product Operations
- Access records within Product Operations
- Read records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, NetSuite ERP, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Intern (Compliance) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Product Intern (APAC Region)

**Role ID:** `RL-PRO-10063`
**Department:** Product
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Zendesk Support Desk (Full Authorization Verified)
- Access HubSpot Marketing (Full Authorization Verified)
- Audit Kubernetes Production Cluster (Full Authorization Verified)
- Examine records within Product Operations
- Access records within Product Operations
- Examine records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, HubSpot Marketing, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Intern (APAC Region) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Product Consultant

**Role ID:** `RL-PRO-20021`
**Department:** Product
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View Snowflake Data Warehouse (Full Authorization Verified)
- Inspect Jira System Admin (Full Authorization Verified)
- Read Workday HRIS (Full Authorization Verified)
- Access Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Inspect records within Product Operations
- Inspect records within Product Operations
- Review records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Jira System Admin, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Consultant needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Product Consultant (Cloud)

**Role ID:** `RL-PRO-20086`
**Department:** Product
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult Jira System Admin (Full Authorization Verified)
- Review Slack Enterprise Grid (Full Authorization Verified)
- Inspect AWS Admin Console (Full Authorization Verified)
- Monitor Staging Environments (Full Authorization Verified)
- Access records within Product Operations
- View records within Product Operations
- Access records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Slack Enterprise Grid, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Consultant (Cloud) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Product Consultant (Infrastructure)

**Role ID:** `RL-PRO-20012`
**Department:** Product
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access HubSpot Marketing (Full Authorization Verified)
- Inspect Jira System Admin (Full Authorization Verified)
- Read GitHub Enterprise Admin (Full Authorization Verified)
- Audit Staging Environments (Full Authorization Verified)
- Audit records within Product Operations
- Examine records within Product Operations
- Read records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Jira System Admin, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Consultant (Infrastructure) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Product Consultant (Enterprise)

**Role ID:** `RL-PRO-20071`
**Department:** Product
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access HubSpot Marketing (Full Authorization Verified)
- Inspect Zendesk Support Desk (Full Authorization Verified)
- Consult Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Monitor CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- View records within Product Operations
- Read records within Product Operations
- Inspect records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Zendesk Support Desk, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Consultant (Enterprise) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Product Consultant (APAC Region)

**Role ID:** `RL-PRO-20038`
**Department:** Product
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Workday HRIS (Full Authorization Verified)
- Inspect AWS Admin Console (Full Authorization Verified)
- View Salesforce CRM (Full Authorization Verified)
- Monitor Jira System Admin (Full Authorization Verified)
- Audit records within Product Operations
- Consult records within Product Operations
- Examine records within Product Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Product team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, AWS Admin Console, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Product Consultant (APAC Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

