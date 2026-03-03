---
title: Operations RBAC Hierarchy
department: operations
role_access: employee,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## Operations Department

The Operations department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Operating Officer (COO)

**Role ID:** `RL-OPE-100012`
**Department:** Operations
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Change Datadog APM (Full Authorization Verified)
- Erase Jira System Admin (Full Authorization Verified)
- Revoke CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Remove HubSpot Marketing (Full Authorization Verified)
- Erase MongoDB User Data Store (Full Authorization Verified)
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- Drop Figma Enterprise (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Remove Workday HRIS (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Erase Kubernetes Production Cluster (Full Authorization Verified)
- Monitor records within Operations Operations
- Consult records within Operations Operations
- Access records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing GitHub Enterprise Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, Jira System Admin, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Operating Officer (COO) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Operating Officer (COO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Operating Officer (COO) (Enterprise)

**Role ID:** `RL-OPE-100076`
**Department:** Operations
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase Staging Environments (Full Authorization Verified)
- Revoke Snowflake Data Warehouse (Full Authorization Verified)
- Purge Azure Active Directory (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Destroy HubSpot Marketing (Full Authorization Verified)
- Update GCP Core Infrastructure (Full Authorization Verified)
- Update Datadog APM (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Drop Splunk Security Logs (Full Authorization Verified)
- Terminate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit AWS Admin Console (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Review records within Operations Operations
- Consult records within Operations Operations
- Consult records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Kubernetes Production Cluster

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Staging Environments, Snowflake Data Warehouse, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Operating Officer (COO) (Enterprise) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Operating Officer (COO) (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Operating Officer (COO) (Infrastructure)

**Role ID:** `RL-OPE-100012`
**Department:** Operations
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Manage Zendesk Support Desk (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Alter Staging Environments (Full Authorization Verified)
- Destroy CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Revoke Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Terminate GitHub Enterprise Admin (Full Authorization Verified)
- Erase Snowflake Data Warehouse (Full Authorization Verified)
- Purge Salesforce CRM (Full Authorization Verified)
- Update Slack Enterprise Grid (Full Authorization Verified)
- Destroy Jira System Admin (Full Authorization Verified)
- Access records within Operations Operations
- Access records within Operations Operations
- Review records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing MongoDB User Data Store

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Datadog APM, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Operating Officer (COO) (Infrastructure) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Operating Officer (COO) (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Chief Operating Officer (COO) (Platform)

**Role ID:** `RL-OPE-100088`
**Department:** Operations
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Update AWS Admin Console (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Purge Kubernetes Production Cluster (Full Authorization Verified)
- Configure Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Drop CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change NetSuite ERP (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Terminate Snowflake Data Warehouse (Full Authorization Verified)
- Purge Datadog APM (Full Authorization Verified)
- Monitor records within Operations Operations
- Inspect records within Operations Operations
- Access records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Staging Environments

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, GCP Core Infrastructure, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Operating Officer (COO) (Platform) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Operating Officer (COO) (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Operating Officer (COO) (Growth)

**Role ID:** `RL-OPE-100017`
**Department:** Operations
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Edit Datadog APM (Full Authorization Verified)
- Purge Splunk Security Logs (Full Authorization Verified)
- Terminate AWS Admin Console (Full Authorization Verified)
- Erase GCP Core Infrastructure (Full Authorization Verified)
- Tweak Figma Enterprise (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Erase MongoDB User Data Store (Full Authorization Verified)
- Drop GitHub Enterprise Admin (Full Authorization Verified)
- Remove Azure Active Directory (Full Authorization Verified)
- Revoke Snowflake Data Warehouse (Full Authorization Verified)
- Purge Slack Enterprise Grid (Full Authorization Verified)
- Monitor records within Operations Operations
- Consult records within Operations Operations
- Review records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Jira System Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, Splunk Security Logs, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Operating Officer (COO) (Growth) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Operating Officer (COO) (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of Operations

**Role ID:** `RL-OPE-90057`
**Department:** Operations
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Update NetSuite ERP (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Destroy AWS Admin Console (Full Authorization Verified)
- Change Jira System Admin (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Destroy Figma Enterprise (Full Authorization Verified)
- Update Kubernetes Production Cluster (Full Authorization Verified)
- Alter Staging Environments (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Slack Enterprise Grid (Full Authorization Verified)
- Erase Salesforce CRM (Full Authorization Verified)
- Read records within Operations Operations
- Audit records within Operations Operations
- Monitor records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Datadog APM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: NetSuite ERP, MongoDB User Data Store, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Operations needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Operations receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### VP of Operations (Analytics)

**Role ID:** `RL-OPE-90015`
**Department:** Operations
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Configure Workday HRIS (Full Authorization Verified)
- Erase Zendesk Support Desk (Full Authorization Verified)
- Terminate NetSuite ERP (Full Authorization Verified)
- Update AWS Admin Console (Full Authorization Verified)
- Remove Slack Enterprise Grid (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Update Staging Environments (Full Authorization Verified)
- Erase Salesforce CRM (Full Authorization Verified)
- Tweak HubSpot Marketing (Full Authorization Verified)
- View records within Operations Operations
- Review records within Operations Operations
- View records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Splunk Security Logs

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Workday HRIS, Zendesk Support Desk, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Operations (Analytics) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Operations (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### VP of Operations (Core)

**Role ID:** `RL-OPE-90083`
**Department:** Operations
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Delete CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Alter Workday HRIS (Full Authorization Verified)
- Revoke Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Purge Salesforce CRM (Full Authorization Verified)
- Configure MongoDB User Data Store (Full Authorization Verified)
- Erase Zendesk Support Desk (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Erase Figma Enterprise (Full Authorization Verified)
- Inspect records within Operations Operations
- Inspect records within Operations Operations
- Read records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Jira System Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), NetSuite ERP, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Operations (Core) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Operations (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### VP of Operations (Cloud)

**Role ID:** `RL-OPE-90029`
**Department:** Operations
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Delete Jira System Admin (Full Authorization Verified)
- Drop Staging Environments (Full Authorization Verified)
- Alter HubSpot Marketing (Full Authorization Verified)
- Terminate Salesforce CRM (Full Authorization Verified)
- Remove Snowflake Data Warehouse (Full Authorization Verified)
- Alter Splunk Security Logs (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Erase Figma Enterprise (Full Authorization Verified)
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Delete Zendesk Support Desk (Full Authorization Verified)
- Audit records within Operations Operations
- Review records within Operations Operations
- Consult records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Kubernetes Production Cluster

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Jira System Admin, Staging Environments, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Operations (Cloud) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Operations (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### VP of Operations (Infrastructure)

**Role ID:** `RL-OPE-90055`
**Department:** Operations
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Terminate Zendesk Support Desk (Full Authorization Verified)
- Delete Datadog APM (Full Authorization Verified)
- Adjust AWS Admin Console (Full Authorization Verified)
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Destroy CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Purge Azure Active Directory (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Access records within Operations Operations
- Monitor records within Operations Operations
- Examine records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Splunk Security Logs

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Zendesk Support Desk, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Operations (Infrastructure) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Operations (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Director of Operations

**Role ID:** `RL-OPE-80028`
**Department:** Operations
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Erase Salesforce CRM (Full Authorization Verified)
- Modify Jira System Admin (Full Authorization Verified)
- Purge Figma Enterprise (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Delete Azure Active Directory (Full Authorization Verified)
- Terminate GCP Core Infrastructure (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Slack Enterprise Grid (Full Authorization Verified)
- Edit Staging Environments (Full Authorization Verified)
- Examine records within Operations Operations
- View records within Operations Operations
- View records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Salesforce CRM, Jira System Admin, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Operations needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Operations receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Director of Operations (North America)

**Role ID:** `RL-OPE-80052`
**Department:** Operations
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Destroy Azure Active Directory (Full Authorization Verified)
- Drop Splunk Security Logs (Full Authorization Verified)
- Manage Jira System Admin (Full Authorization Verified)
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Terminate Zendesk Support Desk (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Adjust MongoDB User Data Store (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Purge Workday HRIS (Full Authorization Verified)
- Audit records within Operations Operations
- Examine records within Operations Operations
- View records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Azure Active Directory, Splunk Security Logs, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Operations (North America) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Operations (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Director of Operations (EMEA Region)

**Role ID:** `RL-OPE-80073`
**Department:** Operations
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Modify Datadog APM (Full Authorization Verified)
- Remove MongoDB User Data Store (Full Authorization Verified)
- Drop CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop NetSuite ERP (Full Authorization Verified)
- Destroy Zendesk Support Desk (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Edit Splunk Security Logs (Full Authorization Verified)
- Edit Kubernetes Production Cluster (Full Authorization Verified)
- Configure Salesforce CRM (Full Authorization Verified)
- Destroy HubSpot Marketing (Full Authorization Verified)
- Audit records within Operations Operations
- Audit records within Operations Operations
- Examine records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, MongoDB User Data Store, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Operations (EMEA Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Operations (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Director of Operations (Compliance)

**Role ID:** `RL-OPE-80017`
**Department:** Operations
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Erase HubSpot Marketing (Full Authorization Verified)
- Change GitHub Enterprise Admin (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Destroy Snowflake Data Warehouse (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Update CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Inspect records within Operations Operations
- Audit records within Operations Operations
- Inspect records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: HubSpot Marketing, GitHub Enterprise Admin, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Operations (Compliance) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Operations (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Director of Operations (Infrastructure)

**Role ID:** `RL-OPE-80012`
**Department:** Operations
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Drop GitHub Enterprise Admin (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Terminate Zendesk Support Desk (Full Authorization Verified)
- Update Figma Enterprise (Full Authorization Verified)
- Revoke GCP Core Infrastructure (Full Authorization Verified)
- Delete Splunk Security Logs (Full Authorization Verified)
- Change Salesforce CRM (Full Authorization Verified)
- Review records within Operations Operations
- Examine records within Operations Operations
- Monitor records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Operations aggregate data.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Snowflake Data Warehouse, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of Operations (Infrastructure) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of Operations (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Operations Manager

**Role ID:** `RL-OPE-70032`
**Department:** Operations
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Change GitHub Enterprise Admin (Full Authorization Verified)
- Create Salesforce CRM (Full Authorization Verified)
- Edit AWS Admin Console (Full Authorization Verified)
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Build Splunk Security Logs (Full Authorization Verified)
- Edit Staging Environments (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Manage HubSpot Marketing (Full Authorization Verified)
- Monitor records within Operations Operations
- Read records within Operations Operations
- Inspect records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Salesforce CRM, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Manager needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Operations Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Operations Manager (EMEA Region)

**Role ID:** `RL-OPE-70099`
**Department:** Operations
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Update MongoDB User Data Store (Full Authorization Verified)
- Generate AWS Admin Console (Full Authorization Verified)
- Edit Jira System Admin (Full Authorization Verified)
- Setup Salesforce CRM (Full Authorization Verified)
- Update Azure Active Directory (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Create Datadog APM (Full Authorization Verified)
- Initialize Snowflake Data Warehouse (Full Authorization Verified)
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- View records within Operations Operations
- Read records within Operations Operations
- Audit records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, AWS Admin Console, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Manager (EMEA Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Operations Manager (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Operations Manager (Core)

**Role ID:** `RL-OPE-70039`
**Department:** Operations
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Create Azure Active Directory (Full Authorization Verified)
- Initialize Staging Environments (Full Authorization Verified)
- Construct Workday HRIS (Full Authorization Verified)
- Build CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Initialize GCP Core Infrastructure (Full Authorization Verified)
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Modify Figma Enterprise (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Inspect records within Operations Operations
- Audit records within Operations Operations
- Audit records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Staging Environments, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Manager (Core) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Operations Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Operations Manager (APAC Region)

**Role ID:** `RL-OPE-70043`
**Department:** Operations
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Construct Jira System Admin (Full Authorization Verified)
- Build Figma Enterprise (Full Authorization Verified)
- Modify Zendesk Support Desk (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Manage AWS Admin Console (Full Authorization Verified)
- Adjust Slack Enterprise Grid (Full Authorization Verified)
- Instantiate Azure Active Directory (Full Authorization Verified)
- Setup GCP Core Infrastructure (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Inspect records within Operations Operations
- Examine records within Operations Operations
- Inspect records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Workday HRIS
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Figma Enterprise, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Manager (APAC Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Operations Manager (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Operations Manager (Growth)

**Role ID:** `RL-OPE-70092`
**Department:** Operations
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Produce Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Tweak NetSuite ERP (Full Authorization Verified)
- Tweak Figma Enterprise (Full Authorization Verified)
- Adjust Azure Active Directory (Full Authorization Verified)
- Setup Workday HRIS (Full Authorization Verified)
- Generate Kubernetes Production Cluster (Full Authorization Verified)
- Generate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Instantiate AWS Admin Console (Full Authorization Verified)
- Review records within Operations Operations
- Consult records within Operations Operations
- Audit records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), NetSuite ERP, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Manager (Growth) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Operations Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Operations Manager

**Role ID:** `RL-OPE-60011`
**Department:** Operations
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust NetSuite ERP (Full Authorization Verified)
- Edit MongoDB User Data Store (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Build AWS Admin Console (Full Authorization Verified)
- Instantiate Splunk Security Logs (Full Authorization Verified)
- Build Workday HRIS (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Produce Kubernetes Production Cluster (Full Authorization Verified)
- Access records within Operations Operations
- Read records within Operations Operations
- Review records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, MongoDB User Data Store, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Manager needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Operations Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Operations Manager (Enterprise)

**Role ID:** `RL-OPE-60031`
**Department:** Operations
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Generate Workday HRIS (Full Authorization Verified)
- Adjust Staging Environments (Full Authorization Verified)
- Create CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Build Jira System Admin (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Produce Zendesk Support Desk (Full Authorization Verified)
- Examine records within Operations Operations
- Examine records within Operations Operations
- View records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Staging Environments, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Manager (Enterprise) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Operations Manager (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Operations Manager (Infrastructure)

**Role ID:** `RL-OPE-60041`
**Department:** Operations
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Configure Jira System Admin (Full Authorization Verified)
- Build Salesforce CRM (Full Authorization Verified)
- Initialize Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Create Workday HRIS (Full Authorization Verified)
- Instantiate GCP Core Infrastructure (Full Authorization Verified)
- Setup Slack Enterprise Grid (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Configure Zendesk Support Desk (Full Authorization Verified)
- Inspect records within Operations Operations
- Examine records within Operations Operations
- Examine records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Salesforce CRM, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Manager (Infrastructure) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Operations Manager (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Operations Manager (Analytics)

**Role ID:** `RL-OPE-60079`
**Department:** Operations
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Configure AWS Admin Console (Full Authorization Verified)
- Instantiate HubSpot Marketing (Full Authorization Verified)
- Instantiate Datadog APM (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Produce Jira System Admin (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Instantiate Splunk Security Logs (Full Authorization Verified)
- Produce GitHub Enterprise Admin (Full Authorization Verified)
- Examine records within Operations Operations
- Monitor records within Operations Operations
- Examine records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, HubSpot Marketing, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Manager (Analytics) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Operations Manager (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Operations Manager (APAC Region)

**Role ID:** `RL-OPE-60063`
**Department:** Operations
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Manage Splunk Security Logs (Full Authorization Verified)
- Setup GCP Core Infrastructure (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Tweak Datadog APM (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- Generate HubSpot Marketing (Full Authorization Verified)
- Examine records within Operations Operations
- Access records within Operations Operations
- Access records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, GCP Core Infrastructure, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Manager (APAC Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Operations Manager (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Operations Lead

**Role ID:** `RL-OPE-50080`
**Department:** Operations
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Instantiate Kubernetes Production Cluster (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Construct Figma Enterprise (Full Authorization Verified)
- Update Slack Enterprise Grid (Full Authorization Verified)
- Setup NetSuite ERP (Full Authorization Verified)
- Generate GitHub Enterprise Admin (Full Authorization Verified)
- Monitor records within Operations Operations
- Consult records within Operations Operations
- Review records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, GCP Core Infrastructure, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Lead needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Operations Lead (Platform)

**Role ID:** `RL-OPE-50097`
**Department:** Operations
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Construct NetSuite ERP (Full Authorization Verified)
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Instantiate HubSpot Marketing (Full Authorization Verified)
- Create Splunk Security Logs (Full Authorization Verified)
- Adjust Zendesk Support Desk (Full Authorization Verified)
- Instantiate Salesforce CRM (Full Authorization Verified)
- Review records within Operations Operations
- Inspect records within Operations Operations
- Consult records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, NetSuite ERP, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Lead (Platform) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Operations Lead (EMEA Region)

**Role ID:** `RL-OPE-50039`
**Department:** Operations
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Tweak Workday HRIS (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Change GitHub Enterprise Admin (Full Authorization Verified)
- Build Slack Enterprise Grid (Full Authorization Verified)
- Create Snowflake Data Warehouse (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Setup Staging Environments (Full Authorization Verified)
- Review records within Operations Operations
- Monitor records within Operations Operations
- Monitor records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, GCP Core Infrastructure, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Lead (EMEA Region) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Operations Lead (Analytics)

**Role ID:** `RL-OPE-50057`
**Department:** Operations
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust Azure Active Directory (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Create GCP Core Infrastructure (Full Authorization Verified)
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust Figma Enterprise (Full Authorization Verified)
- Construct MongoDB User Data Store (Full Authorization Verified)
- Examine records within Operations Operations
- Inspect records within Operations Operations
- View records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Jira System Admin, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Lead (Analytics) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Operations Lead (Cloud)

**Role ID:** `RL-OPE-50078`
**Department:** Operations
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Build HubSpot Marketing (Full Authorization Verified)
- Produce Kubernetes Production Cluster (Full Authorization Verified)
- Construct Slack Enterprise Grid (Full Authorization Verified)
- Produce Staging Environments (Full Authorization Verified)
- Build Splunk Security Logs (Full Authorization Verified)
- Alter Zendesk Support Desk (Full Authorization Verified)
- Instantiate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Read records within Operations Operations
- Consult records within Operations Operations
- View records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Kubernetes Production Cluster, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Operations Lead (Cloud) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Operations Specialist

**Role ID:** `RL-OPE-40013`
**Department:** Operations
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Alter HubSpot Marketing (Full Authorization Verified)
- Initialize Jira System Admin (Full Authorization Verified)
- Manage Azure Active Directory (Full Authorization Verified)
- Configure NetSuite ERP (Full Authorization Verified)
- Produce Datadog APM (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Review records within Operations Operations
- Monitor records within Operations Operations
- Consult records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Jira System Admin, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Specialist needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Operations Specialist (Platform)

**Role ID:** `RL-OPE-40064`
**Department:** Operations
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Alter Splunk Security Logs (Full Authorization Verified)
- Create Zendesk Support Desk (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Configure Staging Environments (Full Authorization Verified)
- View records within Operations Operations
- Monitor records within Operations Operations
- Inspect records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Slack Enterprise Grid, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Specialist (Platform) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Operations Specialist (Core)

**Role ID:** `RL-OPE-40030`
**Department:** Operations
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Setup Workday HRIS (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Instantiate Jira System Admin (Full Authorization Verified)
- Change NetSuite ERP (Full Authorization Verified)
- Generate Staging Environments (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Audit records within Operations Operations
- Examine records within Operations Operations
- Review records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Production Database Cluster (PostgreSQL), Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Specialist (Core) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Operations Specialist (Infrastructure)

**Role ID:** `RL-OPE-40098`
**Department:** Operations
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Manage Datadog APM (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Generate HubSpot Marketing (Full Authorization Verified)
- Construct Figma Enterprise (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Construct Slack Enterprise Grid (Full Authorization Verified)
- Examine records within Operations Operations
- Review records within Operations Operations
- Consult records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, Snowflake Data Warehouse, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Specialist (Infrastructure) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Operations Specialist (Compliance)

**Role ID:** `RL-OPE-40052`
**Department:** Operations
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Tweak Figma Enterprise (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure Salesforce CRM (Full Authorization Verified)
- Update MongoDB User Data Store (Full Authorization Verified)
- Generate Zendesk Support Desk (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Read records within Operations Operations
- Inspect records within Operations Operations
- Read records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, CI/CD Pipelines (Jenkins/GitHub Actions), Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Operations Specialist (Compliance) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Operations Specialist

**Role ID:** `RL-OPE-30032`
**Department:** Operations
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- View GCP Core Infrastructure (Full Authorization Verified)
- Audit Zendesk Support Desk (Full Authorization Verified)
- Examine Workday HRIS (Full Authorization Verified)
- Review AWS Admin Console (Full Authorization Verified)
- Examine records within Operations Operations
- Read records within Operations Operations
- Monitor records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), GCP Core Infrastructure, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Specialist needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Operations Specialist (North America)

**Role ID:** `RL-OPE-30035`
**Department:** Operations
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult Datadog APM (Full Authorization Verified)
- Consult Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Review Staging Environments (Full Authorization Verified)
- Examine Slack Enterprise Grid (Full Authorization Verified)
- Consult Splunk Security Logs (Full Authorization Verified)
- Access records within Operations Operations
- Examine records within Operations Operations
- Read records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, Production Database Cluster (PostgreSQL), Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Specialist (North America) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Operations Specialist (EMEA Region)

**Role ID:** `RL-OPE-30016`
**Department:** Operations
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Slack Enterprise Grid (Full Authorization Verified)
- View GCP Core Infrastructure (Full Authorization Verified)
- Inspect CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- View Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Consult Zendesk Support Desk (Full Authorization Verified)
- View records within Operations Operations
- Read records within Operations Operations
- View records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, GCP Core Infrastructure, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Specialist (EMEA Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Operations Specialist (Infrastructure)

**Role ID:** `RL-OPE-30036`
**Department:** Operations
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult GCP Core Infrastructure (Full Authorization Verified)
- Consult GitHub Enterprise Admin (Full Authorization Verified)
- Monitor Zendesk Support Desk (Full Authorization Verified)
- Review Splunk Security Logs (Full Authorization Verified)
- Review AWS Admin Console (Full Authorization Verified)
- Review records within Operations Operations
- Examine records within Operations Operations
- Read records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, GitHub Enterprise Admin, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Specialist (Infrastructure) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Operations Specialist (North America)

**Role ID:** `RL-OPE-30094`
**Department:** Operations
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View MongoDB User Data Store (Full Authorization Verified)
- Audit Zendesk Support Desk (Full Authorization Verified)
- View HubSpot Marketing (Full Authorization Verified)
- Review GitHub Enterprise Admin (Full Authorization Verified)
- Consult Splunk Security Logs (Full Authorization Verified)
- Monitor records within Operations Operations
- Review records within Operations Operations
- Audit records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Zendesk Support Desk, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Specialist (North America) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Operations Intern

**Role ID:** `RL-OPE-10078`
**Department:** Operations
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult HubSpot Marketing (Full Authorization Verified)
- View AWS Admin Console (Full Authorization Verified)
- Monitor GitHub Enterprise Admin (Full Authorization Verified)
- Monitor records within Operations Operations
- Examine records within Operations Operations
- Read records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, AWS Admin Console, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Intern needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Operations Intern (Cloud)

**Role ID:** `RL-OPE-10020`
**Department:** Operations
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit Workday HRIS (Full Authorization Verified)
- Inspect Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Access HubSpot Marketing (Full Authorization Verified)
- Review records within Operations Operations
- Inspect records within Operations Operations
- View records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Production Database Cluster (PostgreSQL), HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Intern (Cloud) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Operations Intern (Growth)

**Role ID:** `RL-OPE-10037`
**Department:** Operations
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Slack Enterprise Grid (Full Authorization Verified)
- Access Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Inspect Staging Environments (Full Authorization Verified)
- Read records within Operations Operations
- Consult records within Operations Operations
- Access records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Production Database Cluster (PostgreSQL), Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Intern (Growth) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Operations Intern (Compliance)

**Role ID:** `RL-OPE-10080`
**Department:** Operations
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Azure Active Directory (Full Authorization Verified)
- View HubSpot Marketing (Full Authorization Verified)
- Read AWS Admin Console (Full Authorization Verified)
- Monitor records within Operations Operations
- View records within Operations Operations
- Access records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, HubSpot Marketing, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Intern (Compliance) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Operations Intern (Analytics)

**Role ID:** `RL-OPE-10029`
**Department:** Operations
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Staging Environments (Full Authorization Verified)
- Monitor Splunk Security Logs (Full Authorization Verified)
- Audit Figma Enterprise (Full Authorization Verified)
- Audit records within Operations Operations
- Consult records within Operations Operations
- Review records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Splunk Security Logs, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Intern (Analytics) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Operations Consultant

**Role ID:** `RL-OPE-20066`
**Department:** Operations
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit HubSpot Marketing (Full Authorization Verified)
- Read GitHub Enterprise Admin (Full Authorization Verified)
- Consult NetSuite ERP (Full Authorization Verified)
- Consult GCP Core Infrastructure (Full Authorization Verified)
- Examine records within Operations Operations
- Read records within Operations Operations
- Consult records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, GitHub Enterprise Admin, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Consultant needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Operations Consultant (Cloud)

**Role ID:** `RL-OPE-20066`
**Department:** Operations
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access AWS Admin Console (Full Authorization Verified)
- Monitor NetSuite ERP (Full Authorization Verified)
- Consult Staging Environments (Full Authorization Verified)
- Audit Zendesk Support Desk (Full Authorization Verified)
- Audit records within Operations Operations
- Read records within Operations Operations
- Monitor records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, NetSuite ERP, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Consultant (Cloud) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Operations Consultant (Enterprise)

**Role ID:** `RL-OPE-20055`
**Department:** Operations
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View Snowflake Data Warehouse (Full Authorization Verified)
- Review Kubernetes Production Cluster (Full Authorization Verified)
- View CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Read MongoDB User Data Store (Full Authorization Verified)
- Review records within Operations Operations
- Review records within Operations Operations
- Review records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Kubernetes Production Cluster, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Consultant (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Operations Consultant (Platform)

**Role ID:** `RL-OPE-20073`
**Department:** Operations
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read GitHub Enterprise Admin (Full Authorization Verified)
- Review Slack Enterprise Grid (Full Authorization Verified)
- Examine Workday HRIS (Full Authorization Verified)
- Review Datadog APM (Full Authorization Verified)
- Read records within Operations Operations
- Inspect records within Operations Operations
- Inspect records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Slack Enterprise Grid, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Consultant (Platform) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Operations Consultant (Core)

**Role ID:** `RL-OPE-20070`
**Department:** Operations
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor MongoDB User Data Store (Full Authorization Verified)
- Consult Slack Enterprise Grid (Full Authorization Verified)
- Access HubSpot Marketing (Full Authorization Verified)
- Consult Staging Environments (Full Authorization Verified)
- Review records within Operations Operations
- Consult records within Operations Operations
- Review records within Operations Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Operations team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Slack Enterprise Grid, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Operations Consultant (Core) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

