---
title: Engineering RBAC Hierarchy
department: engineering
role_access: engineering,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## Engineering Department

The Engineering department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Technology Officer (CTO)

**Role ID:** `RL-ENG-100035`
**Department:** Engineering
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Update Staging Environments (Full Authorization Verified)
- Terminate Figma Enterprise (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Erase GitHub Enterprise Admin (Full Authorization Verified)
- Revoke Slack Enterprise Grid (Full Authorization Verified)
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Workday HRIS (Full Authorization Verified)
- Delete GCP Core Infrastructure (Full Authorization Verified)
- Erase HubSpot Marketing (Full Authorization Verified)
- Drop Snowflake Data Warehouse (Full Authorization Verified)
- Delete NetSuite ERP (Full Authorization Verified)
- Remove Jira System Admin (Full Authorization Verified)
- Monitor records within Engineering Operations
- Consult records within Engineering Operations
- View records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, Figma Enterprise, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Technology Officer (CTO) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Technology Officer (CTO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Chief Technology Officer (CTO) (Platform)

**Role ID:** `RL-ENG-100023`
**Department:** Engineering
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Terminate Figma Enterprise (Full Authorization Verified)
- Configure Datadog APM (Full Authorization Verified)
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change GCP Core Infrastructure (Full Authorization Verified)
- Remove Kubernetes Production Cluster (Full Authorization Verified)
- Destroy Salesforce CRM (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Delete HubSpot Marketing (Full Authorization Verified)
- Consult records within Engineering Operations
- View records within Engineering Operations
- Read records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing AWS Admin Console

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Slack Enterprise Grid, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Technology Officer (CTO) (Platform) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Technology Officer (CTO) (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Chief Technology Officer (CTO) (Enterprise)

**Role ID:** `RL-ENG-100052`
**Department:** Engineering
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Update Slack Enterprise Grid (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Destroy Workday HRIS (Full Authorization Verified)
- Change AWS Admin Console (Full Authorization Verified)
- Terminate Splunk Security Logs (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Purge GCP Core Infrastructure (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Configure Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Jira System Admin (Full Authorization Verified)
- Remove GitHub Enterprise Admin (Full Authorization Verified)
- Review records within Engineering Operations
- Monitor records within Engineering Operations
- Monitor records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Figma Enterprise

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Slack Enterprise Grid, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Technology Officer (CTO) (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Technology Officer (CTO) (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Chief Technology Officer (CTO) (EMEA Region)

**Role ID:** `RL-ENG-100022`
**Department:** Engineering
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke Slack Enterprise Grid (Full Authorization Verified)
- Modify Salesforce CRM (Full Authorization Verified)
- Destroy Snowflake Data Warehouse (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Revoke Jira System Admin (Full Authorization Verified)
- Drop Zendesk Support Desk (Full Authorization Verified)
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Delete MongoDB User Data Store (Full Authorization Verified)
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Drop AWS Admin Console (Full Authorization Verified)
- Destroy Figma Enterprise (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Inspect records within Engineering Operations
- Monitor records within Engineering Operations
- Consult records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Azure Active Directory

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Salesforce CRM, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Technology Officer (CTO) (EMEA Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Technology Officer (CTO) (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Technology Officer (CTO) (APAC Region)

**Role ID:** `RL-ENG-100019`
**Department:** Engineering
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Tweak AWS Admin Console (Full Authorization Verified)
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Change GCP Core Infrastructure (Full Authorization Verified)
- Tweak Jira System Admin (Full Authorization Verified)
- Configure Slack Enterprise Grid (Full Authorization Verified)
- Remove HubSpot Marketing (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Remove Azure Active Directory (Full Authorization Verified)
- Modify Staging Environments (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Purge Zendesk Support Desk (Full Authorization Verified)
- Inspect records within Engineering Operations
- Examine records within Engineering Operations
- Examine records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, AWS Admin Console, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Technology Officer (CTO) (APAC Region) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Technology Officer (CTO) (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of Engineering

**Role ID:** `RL-ENG-90070`
**Department:** Engineering
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak AWS Admin Console (Full Authorization Verified)
- Drop CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Erase Slack Enterprise Grid (Full Authorization Verified)
- Change NetSuite ERP (Full Authorization Verified)
- Modify Jira System Admin (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Destroy Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Alter Zendesk Support Desk (Full Authorization Verified)
- Read records within Engineering Operations
- Monitor records within Engineering Operations
- Consult records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Azure Active Directory

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, CI/CD Pipelines (Jenkins/GitHub Actions), Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Engineering needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Engineering receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### VP of Engineering (Infrastructure)

**Role ID:** `RL-ENG-90096`
**Department:** Engineering
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Destroy Zendesk Support Desk (Full Authorization Verified)
- Update Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Destroy Staging Environments (Full Authorization Verified)
- Drop NetSuite ERP (Full Authorization Verified)
- Tweak Salesforce CRM (Full Authorization Verified)
- Terminate GCP Core Infrastructure (Full Authorization Verified)
- Erase Slack Enterprise Grid (Full Authorization Verified)
- Erase Figma Enterprise (Full Authorization Verified)
- Terminate Azure Active Directory (Full Authorization Verified)
- Update GitHub Enterprise Admin (Full Authorization Verified)
- Read records within Engineering Operations
- View records within Engineering Operations
- Examine records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing AWS Admin Console

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Production Database Cluster (PostgreSQL), Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Engineering (Infrastructure) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Engineering (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### VP of Engineering (Platform)

**Role ID:** `RL-ENG-90060`
**Department:** Engineering
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Erase Kubernetes Production Cluster (Full Authorization Verified)
- Revoke Azure Active Directory (Full Authorization Verified)
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- Terminate Slack Enterprise Grid (Full Authorization Verified)
- Tweak Datadog APM (Full Authorization Verified)
- Drop GitHub Enterprise Admin (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Drop MongoDB User Data Store (Full Authorization Verified)
- Drop NetSuite ERP (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Review records within Engineering Operations
- Audit records within Engineering Operations
- View records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Staging Environments

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Kubernetes Production Cluster, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Engineering (Platform) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Engineering (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### VP of Engineering (APAC Region)

**Role ID:** `RL-ENG-90093`
**Department:** Engineering
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Remove Workday HRIS (Full Authorization Verified)
- Update Azure Active Directory (Full Authorization Verified)
- Update GCP Core Infrastructure (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Purge Snowflake Data Warehouse (Full Authorization Verified)
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Remove Splunk Security Logs (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Purge Slack Enterprise Grid (Full Authorization Verified)
- Read records within Engineering Operations
- Inspect records within Engineering Operations
- Inspect records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing GitHub Enterprise Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Workday HRIS, Azure Active Directory, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Engineering (APAC Region) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Engineering (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### VP of Engineering (Platform)

**Role ID:** `RL-ENG-90030`
**Department:** Engineering
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase Workday HRIS (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Modify GCP Core Infrastructure (Full Authorization Verified)
- Adjust Jira System Admin (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Destroy Staging Environments (Full Authorization Verified)
- Erase Datadog APM (Full Authorization Verified)
- Erase Azure Active Directory (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- View records within Engineering Operations
- Monitor records within Engineering Operations
- Review records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Salesforce CRM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Workday HRIS, Snowflake Data Warehouse, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Engineering (Platform) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Engineering (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Director of Engineering

**Role ID:** `RL-ENG-80072`
**Department:** Engineering
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Adjust Zendesk Support Desk (Full Authorization Verified)
- Revoke GitHub Enterprise Admin (Full Authorization Verified)
- Purge MongoDB User Data Store (Full Authorization Verified)
- Modify Kubernetes Production Cluster (Full Authorization Verified)
- Revoke HubSpot Marketing (Full Authorization Verified)
- Remove Datadog APM (Full Authorization Verified)
- Revoke Slack Enterprise Grid (Full Authorization Verified)
- Modify AWS Admin Console (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Tweak Workday HRIS (Full Authorization Verified)
- Inspect records within Engineering Operations
- Access records within Engineering Operations
- Read records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, GitHub Enterprise Admin, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Engineering needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Engineering receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Director of Engineering (Core)

**Role ID:** `RL-ENG-80063`
**Department:** Engineering
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Tweak MongoDB User Data Store (Full Authorization Verified)
- Destroy CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Revoke Staging Environments (Full Authorization Verified)
- Revoke Jira System Admin (Full Authorization Verified)
- Delete Slack Enterprise Grid (Full Authorization Verified)
- Update GCP Core Infrastructure (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Edit Splunk Security Logs (Full Authorization Verified)
- Delete HubSpot Marketing (Full Authorization Verified)
- Monitor records within Engineering Operations
- View records within Engineering Operations
- Monitor records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: MongoDB User Data Store, CI/CD Pipelines (Jenkins/GitHub Actions), Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Engineering (Core) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Engineering (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Director of Engineering (EMEA Region)

**Role ID:** `RL-ENG-80095`
**Department:** Engineering
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Configure Staging Environments (Full Authorization Verified)
- Manage Datadog APM (Full Authorization Verified)
- Erase Splunk Security Logs (Full Authorization Verified)
- Erase Salesforce CRM (Full Authorization Verified)
- Revoke Workday HRIS (Full Authorization Verified)
- Remove Figma Enterprise (Full Authorization Verified)
- Modify GitHub Enterprise Admin (Full Authorization Verified)
- Purge NetSuite ERP (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Delete Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Access records within Engineering Operations
- Examine records within Engineering Operations
- Inspect records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, Datadog APM, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Engineering (EMEA Region) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Engineering (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Director of Engineering (Platform)

**Role ID:** `RL-ENG-80038`
**Department:** Engineering
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Modify Staging Environments (Full Authorization Verified)
- Revoke Workday HRIS (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Purge Slack Enterprise Grid (Full Authorization Verified)
- Delete GCP Core Infrastructure (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Terminate Salesforce CRM (Full Authorization Verified)
- Purge AWS Admin Console (Full Authorization Verified)
- Delete CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Examine records within Engineering Operations
- Monitor records within Engineering Operations
- Read records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, Workday HRIS, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Engineering (Platform) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Engineering (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Director of Engineering (Enterprise)

**Role ID:** `RL-ENG-80057`
**Department:** Engineering
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Drop Figma Enterprise (Full Authorization Verified)
- Drop Jira System Admin (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Delete Datadog APM (Full Authorization Verified)
- Purge GCP Core Infrastructure (Full Authorization Verified)
- Remove Azure Active Directory (Full Authorization Verified)
- Adjust Splunk Security Logs (Full Authorization Verified)
- Revoke Workday HRIS (Full Authorization Verified)
- Erase Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View records within Engineering Operations
- Access records within Engineering Operations
- Inspect records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Engineering aggregate data.

#### Systems Access
Authorized platforms: Figma Enterprise, Jira System Admin, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Engineering (Enterprise) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Engineering (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Engineering Manager

**Role ID:** `RL-ENG-70073`
**Department:** Engineering
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Setup Slack Enterprise Grid (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Generate Splunk Security Logs (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Generate Jira System Admin (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Instantiate AWS Admin Console (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Construct Kubernetes Production Cluster (Full Authorization Verified)
- Audit records within Engineering Operations
- Inspect records within Engineering Operations
- Consult records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, MongoDB User Data Store, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Engineering Manager needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Engineering Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Engineering Manager (Infrastructure)

**Role ID:** `RL-ENG-70079`
**Department:** Engineering
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Configure Azure Active Directory (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Build Staging Environments (Full Authorization Verified)
- Construct Snowflake Data Warehouse (Full Authorization Verified)
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Manage GitHub Enterprise Admin (Full Authorization Verified)
- Change MongoDB User Data Store (Full Authorization Verified)
- Edit Splunk Security Logs (Full Authorization Verified)
- Alter AWS Admin Console (Full Authorization Verified)
- Review records within Engineering Operations
- Read records within Engineering Operations
- Consult records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Datadog APM, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Engineering Manager (Infrastructure) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Engineering Manager (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Engineering Manager (Core)

**Role ID:** `RL-ENG-70070`
**Department:** Engineering
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Initialize Jira System Admin (Full Authorization Verified)
- Edit Figma Enterprise (Full Authorization Verified)
- Create Splunk Security Logs (Full Authorization Verified)
- Construct Snowflake Data Warehouse (Full Authorization Verified)
- Build NetSuite ERP (Full Authorization Verified)
- Setup Kubernetes Production Cluster (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Instantiate Datadog APM (Full Authorization Verified)
- Examine records within Engineering Operations
- Review records within Engineering Operations
- Access records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Figma Enterprise, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Engineering Manager (Core) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Engineering Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Engineering Manager (APAC Region)

**Role ID:** `RL-ENG-70069`
**Department:** Engineering
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Build Splunk Security Logs (Full Authorization Verified)
- Update CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Construct Jira System Admin (Full Authorization Verified)
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Adjust Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Initialize GitHub Enterprise Admin (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Adjust Staging Environments (Full Authorization Verified)
- Access records within Engineering Operations
- Monitor records within Engineering Operations
- Read records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, CI/CD Pipelines (Jenkins/GitHub Actions), Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Engineering Manager (APAC Region) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Engineering Manager (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Engineering Manager (Core)

**Role ID:** `RL-ENG-70037`
**Department:** Engineering
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Alter MongoDB User Data Store (Full Authorization Verified)
- Generate Staging Environments (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Update Splunk Security Logs (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Create NetSuite ERP (Full Authorization Verified)
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Access records within Engineering Operations
- Access records within Engineering Operations
- Read records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Staging Environments, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Engineering Manager (Core) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Engineering Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Engineering Manager

**Role ID:** `RL-ENG-60015`
**Department:** Engineering
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Alter Figma Enterprise (Full Authorization Verified)
- Build Workday HRIS (Full Authorization Verified)
- Setup Splunk Security Logs (Full Authorization Verified)
- Create Kubernetes Production Cluster (Full Authorization Verified)
- Alter Zendesk Support Desk (Full Authorization Verified)
- Tweak AWS Admin Console (Full Authorization Verified)
- Modify Salesforce CRM (Full Authorization Verified)
- Instantiate HubSpot Marketing (Full Authorization Verified)
- Audit records within Engineering Operations
- Inspect records within Engineering Operations
- Monitor records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Workday HRIS, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Engineering Manager needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Engineering Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Engineering Manager (Cloud)

**Role ID:** `RL-ENG-60038`
**Department:** Engineering
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Setup MongoDB User Data Store (Full Authorization Verified)
- Setup Azure Active Directory (Full Authorization Verified)
- Generate NetSuite ERP (Full Authorization Verified)
- Build CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Instantiate Slack Enterprise Grid (Full Authorization Verified)
- Create AWS Admin Console (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- Examine records within Engineering Operations
- Audit records within Engineering Operations
- Read records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Azure Active Directory, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Engineering Manager (Cloud) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Engineering Manager (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Engineering Manager (Compliance)

**Role ID:** `RL-ENG-60088`
**Department:** Engineering
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Create Workday HRIS (Full Authorization Verified)
- Instantiate Figma Enterprise (Full Authorization Verified)
- Initialize Staging Environments (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Modify HubSpot Marketing (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Manage CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Build Slack Enterprise Grid (Full Authorization Verified)
- Inspect records within Engineering Operations
- Examine records within Engineering Operations
- Audit records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Figma Enterprise, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Engineering Manager (Compliance) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Engineering Manager (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Engineering Manager (Analytics)

**Role ID:** `RL-ENG-60011`
**Department:** Engineering
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Build Datadog APM (Full Authorization Verified)
- Configure Azure Active Directory (Full Authorization Verified)
- Edit Figma Enterprise (Full Authorization Verified)
- Instantiate Splunk Security Logs (Full Authorization Verified)
- Instantiate GCP Core Infrastructure (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Generate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Monitor records within Engineering Operations
- Monitor records within Engineering Operations
- View records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, Azure Active Directory, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Engineering Manager (Analytics) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Engineering Manager (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Engineering Manager (Analytics)

**Role ID:** `RL-ENG-60090`
**Department:** Engineering
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Create NetSuite ERP (Full Authorization Verified)
- Update Splunk Security Logs (Full Authorization Verified)
- Instantiate Jira System Admin (Full Authorization Verified)
- Create Workday HRIS (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Update GCP Core Infrastructure (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Review records within Engineering Operations
- Examine records within Engineering Operations
- Access records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), NetSuite ERP, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Engineering Manager (Analytics) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Engineering Manager (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Tech Lead

**Role ID:** `RL-ENG-50041`
**Department:** Engineering
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Build Snowflake Data Warehouse (Full Authorization Verified)
- Adjust Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Build AWS Admin Console (Full Authorization Verified)
- Modify Figma Enterprise (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- Read records within Engineering Operations
- Examine records within Engineering Operations
- View records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Production Database Cluster (PostgreSQL), Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Tech Lead needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Tech Lead (Enterprise)

**Role ID:** `RL-ENG-50028`
**Department:** Engineering
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Instantiate GCP Core Infrastructure (Full Authorization Verified)
- Change Jira System Admin (Full Authorization Verified)
- Adjust Splunk Security Logs (Full Authorization Verified)
- Instantiate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Instantiate MongoDB User Data Store (Full Authorization Verified)
- Build NetSuite ERP (Full Authorization Verified)
- Instantiate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Examine records within Engineering Operations
- Examine records within Engineering Operations
- Audit records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Jira System Admin, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Tech Lead (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Tech Lead (Cloud)

**Role ID:** `RL-ENG-50047`
**Department:** Engineering
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Edit Zendesk Support Desk (Full Authorization Verified)
- Change MongoDB User Data Store (Full Authorization Verified)
- Initialize Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Initialize AWS Admin Console (Full Authorization Verified)
- Instantiate Snowflake Data Warehouse (Full Authorization Verified)
- Access records within Engineering Operations
- View records within Engineering Operations
- Inspect records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Splunk Security Logs, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Tech Lead (Cloud) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Tech Lead (North America)

**Role ID:** `RL-ENG-50089`
**Department:** Engineering
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Instantiate MongoDB User Data Store (Full Authorization Verified)
- Setup GCP Core Infrastructure (Full Authorization Verified)
- Build Splunk Security Logs (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Build Kubernetes Production Cluster (Full Authorization Verified)
- Build NetSuite ERP (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Read records within Engineering Operations
- Read records within Engineering Operations
- View records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, GCP Core Infrastructure, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Tech Lead (North America) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Tech Lead (North America)

**Role ID:** `RL-ENG-50055`
**Department:** Engineering
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Produce GCP Core Infrastructure (Full Authorization Verified)
- Build GitHub Enterprise Admin (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Build MongoDB User Data Store (Full Authorization Verified)
- Initialize Datadog APM (Full Authorization Verified)
- Produce Splunk Security Logs (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Review records within Engineering Operations
- Examine records within Engineering Operations
- Inspect records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, GitHub Enterprise Admin, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Tech Lead (North America) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Software Engineer

**Role ID:** `RL-ENG-40093`
**Department:** Engineering
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Update Figma Enterprise (Full Authorization Verified)
- Create Jira System Admin (Full Authorization Verified)
- Generate Splunk Security Logs (Full Authorization Verified)
- Produce NetSuite ERP (Full Authorization Verified)
- Construct GitHub Enterprise Admin (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- View records within Engineering Operations
- Inspect records within Engineering Operations
- Consult records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Jira System Admin, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Software Engineer needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Software Engineer (EMEA Region)

**Role ID:** `RL-ENG-40076`
**Department:** Engineering
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Build NetSuite ERP (Full Authorization Verified)
- Generate Salesforce CRM (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Setup Zendesk Support Desk (Full Authorization Verified)
- Examine records within Engineering Operations
- Read records within Engineering Operations
- Examine records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Kubernetes Production Cluster, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Software Engineer (EMEA Region) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Software Engineer (APAC Region)

**Role ID:** `RL-ENG-40066`
**Department:** Engineering
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Setup Staging Environments (Full Authorization Verified)
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Produce Salesforce CRM (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Initialize GitHub Enterprise Admin (Full Authorization Verified)
- Adjust Azure Active Directory (Full Authorization Verified)
- Access records within Engineering Operations
- Inspect records within Engineering Operations
- Inspect records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Snowflake Data Warehouse, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Software Engineer (APAC Region) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Software Engineer (Analytics)

**Role ID:** `RL-ENG-40080`
**Department:** Engineering
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Build AWS Admin Console (Full Authorization Verified)
- Update Splunk Security Logs (Full Authorization Verified)
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Generate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View records within Engineering Operations
- View records within Engineering Operations
- Access records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Snowflake Data Warehouse, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Software Engineer (Analytics) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Software Engineer (APAC Region)

**Role ID:** `RL-ENG-40040`
**Department:** Engineering
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Alter Azure Active Directory (Full Authorization Verified)
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Instantiate Workday HRIS (Full Authorization Verified)
- Adjust Figma Enterprise (Full Authorization Verified)
- Create Snowflake Data Warehouse (Full Authorization Verified)
- Consult records within Engineering Operations
- Review records within Engineering Operations
- Inspect records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Production Database Cluster (PostgreSQL), MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Software Engineer (APAC Region) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Software Engineer

**Role ID:** `RL-ENG-30086`
**Department:** Engineering
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Salesforce CRM (Full Authorization Verified)
- Audit Slack Enterprise Grid (Full Authorization Verified)
- Monitor Snowflake Data Warehouse (Full Authorization Verified)
- Consult MongoDB User Data Store (Full Authorization Verified)
- View HubSpot Marketing (Full Authorization Verified)
- Monitor records within Engineering Operations
- Inspect records within Engineering Operations
- Review records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, Slack Enterprise Grid, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineer needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Software Engineer (Enterprise)

**Role ID:** `RL-ENG-30032`
**Department:** Engineering
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect HubSpot Marketing (Full Authorization Verified)
- Examine Azure Active Directory (Full Authorization Verified)
- Inspect Workday HRIS (Full Authorization Verified)
- Consult Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Read Zendesk Support Desk (Full Authorization Verified)
- Consult records within Engineering Operations
- Review records within Engineering Operations
- Examine records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Azure Active Directory, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineer (Enterprise) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Software Engineer (Platform)

**Role ID:** `RL-ENG-30088`
**Department:** Engineering
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Snowflake Data Warehouse (Full Authorization Verified)
- Read AWS Admin Console (Full Authorization Verified)
- Access Slack Enterprise Grid (Full Authorization Verified)
- Monitor Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Monitor Datadog APM (Full Authorization Verified)
- Examine records within Engineering Operations
- Read records within Engineering Operations
- Monitor records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, AWS Admin Console, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineer (Platform) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Software Engineer (Platform)

**Role ID:** `RL-ENG-30052`
**Department:** Engineering
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access AWS Admin Console (Full Authorization Verified)
- Read Zendesk Support Desk (Full Authorization Verified)
- Audit GCP Core Infrastructure (Full Authorization Verified)
- Read Splunk Security Logs (Full Authorization Verified)
- Audit Salesforce CRM (Full Authorization Verified)
- Examine records within Engineering Operations
- View records within Engineering Operations
- Audit records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Zendesk Support Desk, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineer (Platform) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Software Engineer (Infrastructure)

**Role ID:** `RL-ENG-30088`
**Department:** Engineering
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Jira System Admin (Full Authorization Verified)
- Review AWS Admin Console (Full Authorization Verified)
- Audit Kubernetes Production Cluster (Full Authorization Verified)
- Inspect HubSpot Marketing (Full Authorization Verified)
- Monitor Workday HRIS (Full Authorization Verified)
- View records within Engineering Operations
- View records within Engineering Operations
- Access records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, AWS Admin Console, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineer (Infrastructure) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Software Engineering Intern

**Role ID:** `RL-ENG-10053`
**Department:** Engineering
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Salesforce CRM (Full Authorization Verified)
- Examine Slack Enterprise Grid (Full Authorization Verified)
- Review Figma Enterprise (Full Authorization Verified)
- Examine records within Engineering Operations
- Access records within Engineering Operations
- Consult records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, Slack Enterprise Grid, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineering Intern needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Software Engineering Intern (Platform)

**Role ID:** `RL-ENG-10045`
**Department:** Engineering
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View AWS Admin Console (Full Authorization Verified)
- Consult Slack Enterprise Grid (Full Authorization Verified)
- Access Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Access records within Engineering Operations
- Audit records within Engineering Operations
- Examine records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Slack Enterprise Grid, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineering Intern (Platform) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Software Engineering Intern (Infrastructure)

**Role ID:** `RL-ENG-10051`
**Department:** Engineering
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Figma Enterprise (Full Authorization Verified)
- Inspect AWS Admin Console (Full Authorization Verified)
- Read GitHub Enterprise Admin (Full Authorization Verified)
- View records within Engineering Operations
- Consult records within Engineering Operations
- Monitor records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, AWS Admin Console, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineering Intern (Infrastructure) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Software Engineering Intern (Infrastructure)

**Role ID:** `RL-ENG-10085`
**Department:** Engineering
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review GCP Core Infrastructure (Full Authorization Verified)
- Examine Snowflake Data Warehouse (Full Authorization Verified)
- Inspect Datadog APM (Full Authorization Verified)
- Consult records within Engineering Operations
- Review records within Engineering Operations
- Review records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Snowflake Data Warehouse, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineering Intern (Infrastructure) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Software Engineering Intern (EMEA Region)

**Role ID:** `RL-ENG-10055`
**Department:** Engineering
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Splunk Security Logs (Full Authorization Verified)
- Review MongoDB User Data Store (Full Authorization Verified)
- Access Staging Environments (Full Authorization Verified)
- Monitor records within Engineering Operations
- Access records within Engineering Operations
- Review records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, MongoDB User Data Store, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Software Engineering Intern (EMEA Region) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Contract Developer

**Role ID:** `RL-ENG-20012`
**Department:** Engineering
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review HubSpot Marketing (Full Authorization Verified)
- Consult CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Examine Salesforce CRM (Full Authorization Verified)
- View MongoDB User Data Store (Full Authorization Verified)
- Inspect records within Engineering Operations
- Monitor records within Engineering Operations
- Monitor records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, CI/CD Pipelines (Jenkins/GitHub Actions), Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Developer needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Contract Developer (Cloud)

**Role ID:** `RL-ENG-20028`
**Department:** Engineering
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Staging Environments (Full Authorization Verified)
- Consult Snowflake Data Warehouse (Full Authorization Verified)
- Monitor Azure Active Directory (Full Authorization Verified)
- Inspect Salesforce CRM (Full Authorization Verified)
- Inspect records within Engineering Operations
- Review records within Engineering Operations
- Access records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Snowflake Data Warehouse, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Developer (Cloud) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Contract Developer (Compliance)

**Role ID:** `RL-ENG-20021`
**Department:** Engineering
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Snowflake Data Warehouse (Full Authorization Verified)
- View MongoDB User Data Store (Full Authorization Verified)
- Examine Splunk Security Logs (Full Authorization Verified)
- Review NetSuite ERP (Full Authorization Verified)
- Consult records within Engineering Operations
- Monitor records within Engineering Operations
- Access records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, MongoDB User Data Store, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Developer (Compliance) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Contract Developer (Analytics)

**Role ID:** `RL-ENG-20058`
**Department:** Engineering
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect MongoDB User Data Store (Full Authorization Verified)
- Examine Splunk Security Logs (Full Authorization Verified)
- Consult HubSpot Marketing (Full Authorization Verified)
- Consult Jira System Admin (Full Authorization Verified)
- View records within Engineering Operations
- Inspect records within Engineering Operations
- Consult records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Splunk Security Logs, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Developer (Analytics) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Contract Developer (Compliance)

**Role ID:** `RL-ENG-20066`
**Department:** Engineering
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect HubSpot Marketing (Full Authorization Verified)
- Monitor AWS Admin Console (Full Authorization Verified)
- View Snowflake Data Warehouse (Full Authorization Verified)
- Inspect Staging Environments (Full Authorization Verified)
- Consult records within Engineering Operations
- Audit records within Engineering Operations
- Read records within Engineering Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Engineering team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, AWS Admin Console, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Contract Developer (Compliance) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

