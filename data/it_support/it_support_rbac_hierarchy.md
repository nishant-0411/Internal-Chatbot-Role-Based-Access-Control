---
title: IT Support RBAC Hierarchy
department: it support
role_access: engineering,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## IT Support Department

The IT Support department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Information Officer (CIO)

**Role ID:** `RL-IT -100092`
**Department:** IT Support
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Destroy GCP Core Infrastructure (Full Authorization Verified)
- Drop CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit Zendesk Support Desk (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Destroy Staging Environments (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Change Workday HRIS (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Update Azure Active Directory (Full Authorization Verified)
- Delete Jira System Admin (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Monitor records within IT Support Operations
- Examine records within IT Support Operations
- Audit records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Kubernetes Production Cluster

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, CI/CD Pipelines (Jenkins/GitHub Actions), Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Officer (CIO) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Officer (CIO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Chief Information Officer (CIO) (Growth)

**Role ID:** `RL-IT -100096`
**Department:** IT Support
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Destroy Kubernetes Production Cluster (Full Authorization Verified)
- Purge Workday HRIS (Full Authorization Verified)
- Destroy Azure Active Directory (Full Authorization Verified)
- Adjust Zendesk Support Desk (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- Remove GitHub Enterprise Admin (Full Authorization Verified)
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Tweak Jira System Admin (Full Authorization Verified)
- Update GCP Core Infrastructure (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Terminate Slack Enterprise Grid (Full Authorization Verified)
- Drop MongoDB User Data Store (Full Authorization Verified)
- View records within IT Support Operations
- Examine records within IT Support Operations
- Review records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Salesforce CRM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Workday HRIS, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Officer (CIO) (Growth) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Officer (CIO) (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Chief Information Officer (CIO) (Growth)

**Role ID:** `RL-IT -100075`
**Department:** IT Support
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Modify Azure Active Directory (Full Authorization Verified)
- Delete GCP Core Infrastructure (Full Authorization Verified)
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Erase Workday HRIS (Full Authorization Verified)
- Revoke GitHub Enterprise Admin (Full Authorization Verified)
- Alter Jira System Admin (Full Authorization Verified)
- Modify Staging Environments (Full Authorization Verified)
- Edit Zendesk Support Desk (Full Authorization Verified)
- Delete CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Revoke HubSpot Marketing (Full Authorization Verified)
- Delete MongoDB User Data Store (Full Authorization Verified)
- Remove Datadog APM (Full Authorization Verified)
- Access records within IT Support Operations
- Inspect records within IT Support Operations
- Audit records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Salesforce CRM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: Azure Active Directory, GCP Core Infrastructure, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Officer (CIO) (Growth) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Officer (CIO) (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Chief Information Officer (CIO) (Analytics)

**Role ID:** `RL-IT -100068`
**Department:** IT Support
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Adjust Figma Enterprise (Full Authorization Verified)
- Revoke Staging Environments (Full Authorization Verified)
- Manage Workday HRIS (Full Authorization Verified)
- Erase Azure Active Directory (Full Authorization Verified)
- Edit Slack Enterprise Grid (Full Authorization Verified)
- Alter AWS Admin Console (Full Authorization Verified)
- Modify Kubernetes Production Cluster (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Revoke Zendesk Support Desk (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- Access records within IT Support Operations
- Monitor records within IT Support Operations
- Examine records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: Figma Enterprise, Staging Environments, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Officer (CIO) (Analytics) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Officer (CIO) (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Information Officer (CIO) (North America)

**Role ID:** `RL-IT -100062`
**Department:** IT Support
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Modify Kubernetes Production Cluster (Full Authorization Verified)
- Purge Figma Enterprise (Full Authorization Verified)
- Destroy Splunk Security Logs (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Destroy Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Adjust AWS Admin Console (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Delete Zendesk Support Desk (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Erase Workday HRIS (Full Authorization Verified)
- Modify GitHub Enterprise Admin (Full Authorization Verified)
- Remove Datadog APM (Full Authorization Verified)
- Monitor records within IT Support Operations
- Consult records within IT Support Operations
- Read records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Azure Active Directory

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Figma Enterprise, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Information Officer (CIO) (North America) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Information Officer (CIO) (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### VP of IT

**Role ID:** `RL-IT -90034`
**Department:** IT Support
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Modify Splunk Security Logs (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Revoke GCP Core Infrastructure (Full Authorization Verified)
- Erase Datadog APM (Full Authorization Verified)
- Drop GitHub Enterprise Admin (Full Authorization Verified)
- Purge Staging Environments (Full Authorization Verified)
- Modify Kubernetes Production Cluster (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Edit Zendesk Support Desk (Full Authorization Verified)
- Destroy Salesforce CRM (Full Authorization Verified)
- View records within IT Support Operations
- Audit records within IT Support Operations
- Review records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Jira System Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: Splunk Security Logs, NetSuite ERP, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of IT needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of IT receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### VP of IT (Enterprise)

**Role ID:** `RL-IT -90035`
**Department:** IT Support
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase GCP Core Infrastructure (Full Authorization Verified)
- Alter Jira System Admin (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Purge Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Delete Staging Environments (Full Authorization Verified)
- Configure Datadog APM (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Purge CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop Splunk Security Logs (Full Authorization Verified)
- Audit records within IT Support Operations
- View records within IT Support Operations
- Examine records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing MongoDB User Data Store

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Jira System Admin, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of IT (Enterprise) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of IT (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### VP of IT (Core)

**Role ID:** `RL-IT -90081`
**Department:** IT Support
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Remove NetSuite ERP (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Purge HubSpot Marketing (Full Authorization Verified)
- Manage Figma Enterprise (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Adjust Azure Active Directory (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Delete Staging Environments (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Purge Splunk Security Logs (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect records within IT Support Operations
- Audit records within IT Support Operations
- Monitor records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: NetSuite ERP, Workday HRIS, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of IT (Core) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of IT (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### VP of IT (EMEA Region)

**Role ID:** `RL-IT -90040`
**Department:** IT Support
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Configure Salesforce CRM (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Alter Splunk Security Logs (Full Authorization Verified)
- Delete GitHub Enterprise Admin (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Revoke Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Revoke Snowflake Data Warehouse (Full Authorization Verified)
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Modify HubSpot Marketing (Full Authorization Verified)
- Erase AWS Admin Console (Full Authorization Verified)
- Audit records within IT Support Operations
- Read records within IT Support Operations
- Audit records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Slack Enterprise Grid

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: Salesforce CRM, Datadog APM, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of IT (EMEA Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of IT (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### VP of IT (Enterprise)

**Role ID:** `RL-IT -90027`
**Department:** IT Support
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke Salesforce CRM (Full Authorization Verified)
- Revoke Datadog APM (Full Authorization Verified)
- Manage GitHub Enterprise Admin (Full Authorization Verified)
- Terminate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Drop GCP Core Infrastructure (Full Authorization Verified)
- Delete Jira System Admin (Full Authorization Verified)
- Terminate NetSuite ERP (Full Authorization Verified)
- Delete Azure Active Directory (Full Authorization Verified)
- Purge Snowflake Data Warehouse (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Audit records within IT Support Operations
- Review records within IT Support Operations
- Monitor records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Zendesk Support Desk

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: Salesforce CRM, Datadog APM, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of IT (Enterprise) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of IT (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Director of IT Support

**Role ID:** `RL-IT -80041`
**Department:** IT Support
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Erase HubSpot Marketing (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Purge Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Drop CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change AWS Admin Console (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Remove Staging Environments (Full Authorization Verified)
- Erase Splunk Security Logs (Full Authorization Verified)
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Access records within IT Support Operations
- View records within IT Support Operations
- Inspect records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: HubSpot Marketing, Salesforce CRM, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of IT Support needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of IT Support receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Director of IT Support (EMEA Region)

**Role ID:** `RL-IT -80094`
**Department:** IT Support
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Delete NetSuite ERP (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Update Staging Environments (Full Authorization Verified)
- Destroy Workday HRIS (Full Authorization Verified)
- Revoke HubSpot Marketing (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Revoke GCP Core Infrastructure (Full Authorization Verified)
- Audit records within IT Support Operations
- Consult records within IT Support Operations
- Consult records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, NetSuite ERP, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of IT Support (EMEA Region) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of IT Support (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Director of IT Support (Platform)

**Role ID:** `RL-IT -80056`
**Department:** IT Support
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Destroy CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Destroy NetSuite ERP (Full Authorization Verified)
- Revoke Slack Enterprise Grid (Full Authorization Verified)
- Delete Splunk Security Logs (Full Authorization Verified)
- Alter Jira System Admin (Full Authorization Verified)
- Manage Zendesk Support Desk (Full Authorization Verified)
- Erase HubSpot Marketing (Full Authorization Verified)
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Consult records within IT Support Operations
- Audit records within IT Support Operations
- Examine records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Datadog APM, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of IT Support (Platform) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of IT Support (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Director of IT Support (EMEA Region)

**Role ID:** `RL-IT -80035`
**Department:** IT Support
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Configure AWS Admin Console (Full Authorization Verified)
- Erase Datadog APM (Full Authorization Verified)
- Configure MongoDB User Data Store (Full Authorization Verified)
- Update Slack Enterprise Grid (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Remove Jira System Admin (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Alter Zendesk Support Desk (Full Authorization Verified)
- Monitor records within IT Support Operations
- Access records within IT Support Operations
- Inspect records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, Datadog APM, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of IT Support (EMEA Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of IT Support (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Director of IT Support (Enterprise)

**Role ID:** `RL-IT -80043`
**Department:** IT Support
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Revoke Zendesk Support Desk (Full Authorization Verified)
- Configure Azure Active Directory (Full Authorization Verified)
- Destroy GCP Core Infrastructure (Full Authorization Verified)
- Terminate Salesforce CRM (Full Authorization Verified)
- Manage Datadog APM (Full Authorization Verified)
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Terminate NetSuite ERP (Full Authorization Verified)
- Delete GitHub Enterprise Admin (Full Authorization Verified)
- Delete MongoDB User Data Store (Full Authorization Verified)
- Access records within IT Support Operations
- Access records within IT Support Operations
- Examine records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and IT Support aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Zendesk Support Desk, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of IT Support (Enterprise) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of IT Support (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior IT Manager

**Role ID:** `RL-IT -70043`
**Department:** IT Support
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Build Figma Enterprise (Full Authorization Verified)
- Configure Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- Instantiate Datadog APM (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Generate Kubernetes Production Cluster (Full Authorization Verified)
- Configure Staging Environments (Full Authorization Verified)
- Initialize Salesforce CRM (Full Authorization Verified)
- Adjust Azure Active Directory (Full Authorization Verified)
- Examine records within IT Support Operations
- Audit records within IT Support Operations
- Examine records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Production Database Cluster (PostgreSQL), NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior IT Manager needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior IT Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior IT Manager (Infrastructure)

**Role ID:** `RL-IT -70011`
**Department:** IT Support
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Generate GCP Core Infrastructure (Full Authorization Verified)
- Initialize Azure Active Directory (Full Authorization Verified)
- Edit AWS Admin Console (Full Authorization Verified)
- Build HubSpot Marketing (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Build Datadog APM (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Adjust Jira System Admin (Full Authorization Verified)
- Manage CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Examine records within IT Support Operations
- Inspect records within IT Support Operations
- Examine records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Azure Active Directory, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior IT Manager (Infrastructure) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior IT Manager (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior IT Manager (Cloud)

**Role ID:** `RL-IT -70056`
**Department:** IT Support
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Adjust Azure Active Directory (Full Authorization Verified)
- Initialize Kubernetes Production Cluster (Full Authorization Verified)
- Produce Staging Environments (Full Authorization Verified)
- Initialize Splunk Security Logs (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Tweak Figma Enterprise (Full Authorization Verified)
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Create AWS Admin Console (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Review records within IT Support Operations
- Examine records within IT Support Operations
- Read records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Kubernetes Production Cluster, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior IT Manager (Cloud) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior IT Manager (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior IT Manager (Platform)

**Role ID:** `RL-IT -70026`
**Department:** IT Support
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Instantiate Kubernetes Production Cluster (Full Authorization Verified)
- Alter HubSpot Marketing (Full Authorization Verified)
- Setup CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Adjust Jira System Admin (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Modify Staging Environments (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Generate Azure Active Directory (Full Authorization Verified)
- Read records within IT Support Operations
- Review records within IT Support Operations
- Access records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, HubSpot Marketing, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior IT Manager (Platform) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior IT Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior IT Manager (Platform)

**Role ID:** `RL-IT -70071`
**Department:** IT Support
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Update Figma Enterprise (Full Authorization Verified)
- Update CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Instantiate Datadog APM (Full Authorization Verified)
- Setup MongoDB User Data Store (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Construct Workday HRIS (Full Authorization Verified)
- Audit records within IT Support Operations
- Access records within IT Support Operations
- Monitor records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, CI/CD Pipelines (Jenkins/GitHub Actions), HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior IT Manager (Platform) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior IT Manager (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### IT Manager

**Role ID:** `RL-IT -60036`
**Department:** IT Support
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Create Zendesk Support Desk (Full Authorization Verified)
- Adjust Workday HRIS (Full Authorization Verified)
- Setup Splunk Security Logs (Full Authorization Verified)
- Build GitHub Enterprise Admin (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Tweak Figma Enterprise (Full Authorization Verified)
- Instantiate Kubernetes Production Cluster (Full Authorization Verified)
- Produce Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Review records within IT Support Operations
- Examine records within IT Support Operations
- Consult records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Workday HRIS, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A IT Manager needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The IT Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### IT Manager (Growth)

**Role ID:** `RL-IT -60022`
**Department:** IT Support
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Alter Jira System Admin (Full Authorization Verified)
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Create Staging Environments (Full Authorization Verified)
- Instantiate Snowflake Data Warehouse (Full Authorization Verified)
- Create HubSpot Marketing (Full Authorization Verified)
- Instantiate Figma Enterprise (Full Authorization Verified)
- Setup NetSuite ERP (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View records within IT Support Operations
- Access records within IT Support Operations
- Audit records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Slack Enterprise Grid, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A IT Manager (Growth) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The IT Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### IT Manager (Core)

**Role ID:** `RL-IT -60079`
**Department:** IT Support
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Configure Salesforce CRM (Full Authorization Verified)
- Construct HubSpot Marketing (Full Authorization Verified)
- Create Figma Enterprise (Full Authorization Verified)
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Instantiate GCP Core Infrastructure (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Construct Azure Active Directory (Full Authorization Verified)
- Produce GitHub Enterprise Admin (Full Authorization Verified)
- Monitor records within IT Support Operations
- Consult records within IT Support Operations
- Consult records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, HubSpot Marketing, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A IT Manager (Core) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The IT Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### IT Manager (Compliance)

**Role ID:** `RL-IT -60039`
**Department:** IT Support
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Configure Workday HRIS (Full Authorization Verified)
- Generate NetSuite ERP (Full Authorization Verified)
- Setup Figma Enterprise (Full Authorization Verified)
- Setup Salesforce CRM (Full Authorization Verified)
- Build Azure Active Directory (Full Authorization Verified)
- Generate Splunk Security Logs (Full Authorization Verified)
- Construct MongoDB User Data Store (Full Authorization Verified)
- Modify Datadog APM (Full Authorization Verified)
- Read records within IT Support Operations
- Read records within IT Support Operations
- Consult records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, NetSuite ERP, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A IT Manager (Compliance) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The IT Manager (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### IT Manager (APAC Region)

**Role ID:** `RL-IT -60070`
**Department:** IT Support
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Instantiate MongoDB User Data Store (Full Authorization Verified)
- Initialize HubSpot Marketing (Full Authorization Verified)
- Instantiate Staging Environments (Full Authorization Verified)
- Initialize Azure Active Directory (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Generate Snowflake Data Warehouse (Full Authorization Verified)
- Access records within IT Support Operations
- Consult records within IT Support Operations
- Audit records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, HubSpot Marketing, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A IT Manager (APAC Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The IT Manager (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Service Desk Lead

**Role ID:** `RL-IT -50096`
**Department:** IT Support
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Setup Kubernetes Production Cluster (Full Authorization Verified)
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Create Slack Enterprise Grid (Full Authorization Verified)
- Tweak Datadog APM (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- View records within IT Support Operations
- Audit records within IT Support Operations
- View records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, GCP Core Infrastructure, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Service Desk Lead needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Service Desk Lead (Enterprise)

**Role ID:** `RL-IT -50043`
**Department:** IT Support
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Initialize MongoDB User Data Store (Full Authorization Verified)
- Construct CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Construct Kubernetes Production Cluster (Full Authorization Verified)
- Configure Splunk Security Logs (Full Authorization Verified)
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Generate NetSuite ERP (Full Authorization Verified)
- Edit Azure Active Directory (Full Authorization Verified)
- Consult records within IT Support Operations
- Consult records within IT Support Operations
- Audit records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, CI/CD Pipelines (Jenkins/GitHub Actions), Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Service Desk Lead (Enterprise) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Service Desk Lead (North America)

**Role ID:** `RL-IT -50056`
**Department:** IT Support
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Instantiate Datadog APM (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Construct Slack Enterprise Grid (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Instantiate Staging Environments (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Generate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Review records within IT Support Operations
- Read records within IT Support Operations
- Monitor records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, GCP Core Infrastructure, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Service Desk Lead (North America) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Service Desk Lead (Analytics)

**Role ID:** `RL-IT -50073`
**Department:** IT Support
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Construct AWS Admin Console (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Create NetSuite ERP (Full Authorization Verified)
- Create GitHub Enterprise Admin (Full Authorization Verified)
- Generate Salesforce CRM (Full Authorization Verified)
- Generate Datadog APM (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Review records within IT Support Operations
- Examine records within IT Support Operations
- Read records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Workday HRIS, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Service Desk Lead (Analytics) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Service Desk Lead (EMEA Region)

**Role ID:** `RL-IT -50074`
**Department:** IT Support
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Generate Kubernetes Production Cluster (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Build MongoDB User Data Store (Full Authorization Verified)
- Setup Figma Enterprise (Full Authorization Verified)
- Modify Zendesk Support Desk (Full Authorization Verified)
- Instantiate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Access records within IT Support Operations
- Read records within IT Support Operations
- Review records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Kubernetes Production Cluster, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Service Desk Lead (EMEA Region) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Systems Administrator

**Role ID:** `RL-IT -40069`
**Department:** IT Support
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Construct HubSpot Marketing (Full Authorization Verified)
- Create Salesforce CRM (Full Authorization Verified)
- Construct Staging Environments (Full Authorization Verified)
- Create AWS Admin Console (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Produce CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Monitor records within IT Support Operations
- Inspect records within IT Support Operations
- Review records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Salesforce CRM, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Systems Administrator needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Systems Administrator (Infrastructure)

**Role ID:** `RL-IT -40095`
**Department:** IT Support
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Produce Workday HRIS (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Construct Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Generate MongoDB User Data Store (Full Authorization Verified)
- Setup GitHub Enterprise Admin (Full Authorization Verified)
- Setup Kubernetes Production Cluster (Full Authorization Verified)
- Examine records within IT Support Operations
- Audit records within IT Support Operations
- Read records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Figma Enterprise, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Systems Administrator (Infrastructure) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Systems Administrator (Platform)

**Role ID:** `RL-IT -40040`
**Department:** IT Support
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Create Slack Enterprise Grid (Full Authorization Verified)
- Create NetSuite ERP (Full Authorization Verified)
- Generate Figma Enterprise (Full Authorization Verified)
- Adjust Jira System Admin (Full Authorization Verified)
- Edit Snowflake Data Warehouse (Full Authorization Verified)
- Manage Splunk Security Logs (Full Authorization Verified)
- View records within IT Support Operations
- Examine records within IT Support Operations
- Examine records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, NetSuite ERP, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Systems Administrator (Platform) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Systems Administrator (North America)

**Role ID:** `RL-IT -40053`
**Department:** IT Support
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Produce CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Modify Datadog APM (Full Authorization Verified)
- Modify Zendesk Support Desk (Full Authorization Verified)
- Alter Splunk Security Logs (Full Authorization Verified)
- Initialize GCP Core Infrastructure (Full Authorization Verified)
- Audit records within IT Support Operations
- Examine records within IT Support Operations
- Inspect records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Jira System Admin, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Systems Administrator (North America) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Systems Administrator (Platform)

**Role ID:** `RL-IT -40092`
**Department:** IT Support
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Configure Zendesk Support Desk (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- Instantiate Slack Enterprise Grid (Full Authorization Verified)
- Construct MongoDB User Data Store (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Modify Kubernetes Production Cluster (Full Authorization Verified)
- Access records within IT Support Operations
- Audit records within IT Support Operations
- View records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Splunk Security Logs, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Systems Administrator (Platform) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### IT Support Specialist

**Role ID:** `RL-IT -30015`
**Department:** IT Support
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Read Staging Environments (Full Authorization Verified)
- Audit Slack Enterprise Grid (Full Authorization Verified)
- Consult MongoDB User Data Store (Full Authorization Verified)
- Examine Splunk Security Logs (Full Authorization Verified)
- Access records within IT Support Operations
- Examine records within IT Support Operations
- View records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Staging Environments, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Specialist needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### IT Support Specialist (Infrastructure)

**Role ID:** `RL-IT -30083`
**Department:** IT Support
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View GitHub Enterprise Admin (Full Authorization Verified)
- View GCP Core Infrastructure (Full Authorization Verified)
- Access Azure Active Directory (Full Authorization Verified)
- Examine HubSpot Marketing (Full Authorization Verified)
- Examine CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Examine records within IT Support Operations
- Read records within IT Support Operations
- Inspect records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, GCP Core Infrastructure, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Specialist (Infrastructure) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### IT Support Specialist (APAC Region)

**Role ID:** `RL-IT -30044`
**Department:** IT Support
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Examine Snowflake Data Warehouse (Full Authorization Verified)
- Consult MongoDB User Data Store (Full Authorization Verified)
- View GitHub Enterprise Admin (Full Authorization Verified)
- Inspect Datadog APM (Full Authorization Verified)
- Inspect records within IT Support Operations
- Read records within IT Support Operations
- Audit records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Snowflake Data Warehouse, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Specialist (APAC Region) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### IT Support Specialist (Analytics)

**Role ID:** `RL-IT -30050`
**Department:** IT Support
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Splunk Security Logs (Full Authorization Verified)
- Monitor GitHub Enterprise Admin (Full Authorization Verified)
- Consult Azure Active Directory (Full Authorization Verified)
- Access CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Read Kubernetes Production Cluster (Full Authorization Verified)
- Access records within IT Support Operations
- Examine records within IT Support Operations
- Audit records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, GitHub Enterprise Admin, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Specialist (Analytics) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### IT Support Specialist (Growth)

**Role ID:** `RL-IT -30031`
**Department:** IT Support
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View Kubernetes Production Cluster (Full Authorization Verified)
- View Jira System Admin (Full Authorization Verified)
- Consult Splunk Security Logs (Full Authorization Verified)
- Inspect Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Inspect Snowflake Data Warehouse (Full Authorization Verified)
- Audit records within IT Support Operations
- Review records within IT Support Operations
- View records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Jira System Admin, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Specialist (Growth) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### IT Intern

**Role ID:** `RL-IT -10039`
**Department:** IT Support
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View GCP Core Infrastructure (Full Authorization Verified)
- Inspect Jira System Admin (Full Authorization Verified)
- Access HubSpot Marketing (Full Authorization Verified)
- Consult records within IT Support Operations
- View records within IT Support Operations
- Examine records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Jira System Admin, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Intern needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### IT Intern (EMEA Region)

**Role ID:** `RL-IT -10012`
**Department:** IT Support
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Azure Active Directory (Full Authorization Verified)
- View AWS Admin Console (Full Authorization Verified)
- Consult Splunk Security Logs (Full Authorization Verified)
- Review records within IT Support Operations
- Examine records within IT Support Operations
- Inspect records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, AWS Admin Console, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Intern (EMEA Region) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### IT Intern (Infrastructure)

**Role ID:** `RL-IT -10031`
**Department:** IT Support
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Salesforce CRM (Full Authorization Verified)
- Examine GitHub Enterprise Admin (Full Authorization Verified)
- Audit NetSuite ERP (Full Authorization Verified)
- Review records within IT Support Operations
- Inspect records within IT Support Operations
- Monitor records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, GitHub Enterprise Admin, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Intern (Infrastructure) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### IT Intern (Compliance)

**Role ID:** `RL-IT -10012`
**Department:** IT Support
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit Datadog APM (Full Authorization Verified)
- Review MongoDB User Data Store (Full Authorization Verified)
- Audit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Monitor records within IT Support Operations
- Audit records within IT Support Operations
- Inspect records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, MongoDB User Data Store, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Intern (Compliance) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### IT Intern (APAC Region)

**Role ID:** `RL-IT -10060`
**Department:** IT Support
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Salesforce CRM (Full Authorization Verified)
- Monitor CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- View AWS Admin Console (Full Authorization Verified)
- Access records within IT Support Operations
- Review records within IT Support Operations
- Review records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, CI/CD Pipelines (Jenkins/GitHub Actions), AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Intern (APAC Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### IT Support Contractor

**Role ID:** `RL-IT -20023`
**Department:** IT Support
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Salesforce CRM (Full Authorization Verified)
- Consult Staging Environments (Full Authorization Verified)
- Monitor Workday HRIS (Full Authorization Verified)
- Examine Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Audit records within IT Support Operations
- Read records within IT Support Operations
- Examine records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, Staging Environments, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Contractor needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### IT Support Contractor (Analytics)

**Role ID:** `RL-IT -20081`
**Department:** IT Support
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine NetSuite ERP (Full Authorization Verified)
- Review Workday HRIS (Full Authorization Verified)
- Inspect Salesforce CRM (Full Authorization Verified)
- Monitor MongoDB User Data Store (Full Authorization Verified)
- Audit records within IT Support Operations
- View records within IT Support Operations
- Review records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, Workday HRIS, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Contractor (Analytics) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### IT Support Contractor (Compliance)

**Role ID:** `RL-IT -20065`
**Department:** IT Support
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect NetSuite ERP (Full Authorization Verified)
- Examine Staging Environments (Full Authorization Verified)
- Review Workday HRIS (Full Authorization Verified)
- Inspect GitHub Enterprise Admin (Full Authorization Verified)
- Consult records within IT Support Operations
- Examine records within IT Support Operations
- View records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, Staging Environments, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Contractor (Compliance) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### IT Support Contractor (APAC Region)

**Role ID:** `RL-IT -20058`
**Department:** IT Support
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Jira System Admin (Full Authorization Verified)
- Monitor NetSuite ERP (Full Authorization Verified)
- Inspect Staging Environments (Full Authorization Verified)
- Inspect Workday HRIS (Full Authorization Verified)
- Consult records within IT Support Operations
- Access records within IT Support Operations
- Inspect records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, NetSuite ERP, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Contractor (APAC Region) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### IT Support Contractor (North America)

**Role ID:** `RL-IT -20012`
**Department:** IT Support
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect Kubernetes Production Cluster (Full Authorization Verified)
- Read GitHub Enterprise Admin (Full Authorization Verified)
- Examine Splunk Security Logs (Full Authorization Verified)
- Consult records within IT Support Operations
- Read records within IT Support Operations
- Access records within IT Support Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to IT Support team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Kubernetes Production Cluster, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A IT Support Contractor (North America) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

