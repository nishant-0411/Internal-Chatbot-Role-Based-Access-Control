---
title: HR RBAC Hierarchy
department: hr
role_access: hr,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## HR Department

The HR department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Human Resources Officer (CHRO)

**Role ID:** `RL-HR-100086`
**Department:** HR
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke NetSuite ERP (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Delete HubSpot Marketing (Full Authorization Verified)
- Edit CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Drop Datadog APM (Full Authorization Verified)
- Delete GCP Core Infrastructure (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Remove Workday HRIS (Full Authorization Verified)
- Erase Azure Active Directory (Full Authorization Verified)
- Manage AWS Admin Console (Full Authorization Verified)
- Revoke Zendesk Support Desk (Full Authorization Verified)
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Read records within HR Operations
- Monitor records within HR Operations
- Read records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Staging Environments

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: NetSuite ERP, MongoDB User Data Store, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Human Resources Officer (CHRO) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Human Resources Officer (CHRO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Chief Human Resources Officer (CHRO) (EMEA Region)

**Role ID:** `RL-HR-100086`
**Department:** HR
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke Workday HRIS (Full Authorization Verified)
- Terminate GitHub Enterprise Admin (Full Authorization Verified)
- Update Jira System Admin (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Delete Snowflake Data Warehouse (Full Authorization Verified)
- Purge Splunk Security Logs (Full Authorization Verified)
- Edit Azure Active Directory (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Remove Figma Enterprise (Full Authorization Verified)
- Delete Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Drop Staging Environments (Full Authorization Verified)
- Read records within HR Operations
- Audit records within HR Operations
- View records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing AWS Admin Console

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: Workday HRIS, GitHub Enterprise Admin, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Human Resources Officer (CHRO) (EMEA Region) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Human Resources Officer (CHRO) (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Chief Human Resources Officer (CHRO) (APAC Region)

**Role ID:** `RL-HR-100072`
**Department:** HR
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Destroy HubSpot Marketing (Full Authorization Verified)
- Drop GCP Core Infrastructure (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Purge Jira System Admin (Full Authorization Verified)
- Delete Zendesk Support Desk (Full Authorization Verified)
- Remove AWS Admin Console (Full Authorization Verified)
- Update Slack Enterprise Grid (Full Authorization Verified)
- Configure NetSuite ERP (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Inspect records within HR Operations
- Inspect records within HR Operations
- View records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Salesforce CRM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Workday HRIS, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Human Resources Officer (CHRO) (APAC Region) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Human Resources Officer (CHRO) (APAC Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Chief Human Resources Officer (CHRO) (Enterprise)

**Role ID:** `RL-HR-100059`
**Department:** HR
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase GCP Core Infrastructure (Full Authorization Verified)
- Terminate NetSuite ERP (Full Authorization Verified)
- Modify Figma Enterprise (Full Authorization Verified)
- Revoke Splunk Security Logs (Full Authorization Verified)
- Remove Snowflake Data Warehouse (Full Authorization Verified)
- Destroy Azure Active Directory (Full Authorization Verified)
- Destroy Staging Environments (Full Authorization Verified)
- Adjust CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Manage AWS Admin Console (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Review records within HR Operations
- Review records within HR Operations
- Consult records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Slack Enterprise Grid

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, NetSuite ERP, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Human Resources Officer (CHRO) (Enterprise) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Human Resources Officer (CHRO) (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Chief Human Resources Officer (CHRO) (Platform)

**Role ID:** `RL-HR-100096`
**Department:** HR
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke Datadog APM (Full Authorization Verified)
- Configure Salesforce CRM (Full Authorization Verified)
- Erase Azure Active Directory (Full Authorization Verified)
- Change Workday HRIS (Full Authorization Verified)
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Erase NetSuite ERP (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Erase AWS Admin Console (Full Authorization Verified)
- Tweak Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Purge Staging Environments (Full Authorization Verified)
- Erase Splunk Security Logs (Full Authorization Verified)
- Monitor records within HR Operations
- Monitor records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Slack Enterprise Grid

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, Salesforce CRM, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Human Resources Officer (CHRO) (Platform) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Human Resources Officer (CHRO) (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### VP of HR

**Role ID:** `RL-HR-90061`
**Department:** HR
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Manage Azure Active Directory (Full Authorization Verified)
- Purge Kubernetes Production Cluster (Full Authorization Verified)
- Alter Slack Enterprise Grid (Full Authorization Verified)
- Edit Jira System Admin (Full Authorization Verified)
- Configure Splunk Security Logs (Full Authorization Verified)
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Tweak Workday HRIS (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Purge Figma Enterprise (Full Authorization Verified)
- Destroy NetSuite ERP (Full Authorization Verified)
- Consult records within HR Operations
- Access records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Datadog APM

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: Azure Active Directory, Kubernetes Production Cluster, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of HR needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of HR receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### VP of HR (Analytics)

**Role ID:** `RL-HR-90050`
**Department:** HR
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Destroy Salesforce CRM (Full Authorization Verified)
- Change Snowflake Data Warehouse (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Manage Kubernetes Production Cluster (Full Authorization Verified)
- Configure MongoDB User Data Store (Full Authorization Verified)
- Purge Jira System Admin (Full Authorization Verified)
- Erase Staging Environments (Full Authorization Verified)
- Modify HubSpot Marketing (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- Examine records within HR Operations
- Examine records within HR Operations
- Monitor records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Figma Enterprise

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), AWS Admin Console, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of HR (Analytics) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of HR (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### VP of HR (Enterprise)

**Role ID:** `RL-HR-90098`
**Department:** HR
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Revoke CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Destroy Figma Enterprise (Full Authorization Verified)
- Delete GitHub Enterprise Admin (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Destroy Workday HRIS (Full Authorization Verified)
- Adjust Zendesk Support Desk (Full Authorization Verified)
- Configure Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Remove Salesforce CRM (Full Authorization Verified)
- Erase Azure Active Directory (Full Authorization Verified)
- Read records within HR Operations
- Monitor records within HR Operations
- Consult records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing AWS Admin Console

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Staging Environments, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of HR (Enterprise) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of HR (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of HR (Analytics)

**Role ID:** `RL-HR-90035`
**Department:** HR
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Tweak Snowflake Data Warehouse (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Tweak Workday HRIS (Full Authorization Verified)
- Tweak Zendesk Support Desk (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Revoke AWS Admin Console (Full Authorization Verified)
- Drop Slack Enterprise Grid (Full Authorization Verified)
- Change GCP Core Infrastructure (Full Authorization Verified)
- Edit Azure Active Directory (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Audit records within HR Operations
- Inspect records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Staging Environments, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of HR (Analytics) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of HR (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of HR (Platform)

**Role ID:** `RL-HR-90081`
**Department:** HR
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Change Salesforce CRM (Full Authorization Verified)
- Erase AWS Admin Console (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Terminate Zendesk Support Desk (Full Authorization Verified)
- Purge Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Erase Snowflake Data Warehouse (Full Authorization Verified)
- Purge GitHub Enterprise Admin (Full Authorization Verified)
- Remove Datadog APM (Full Authorization Verified)
- Destroy Figma Enterprise (Full Authorization Verified)
- Drop Splunk Security Logs (Full Authorization Verified)
- Destroy HubSpot Marketing (Full Authorization Verified)
- Monitor records within HR Operations
- Monitor records within HR Operations
- Audit records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Azure Active Directory

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: Salesforce CRM, AWS Admin Console, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of HR (Platform) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of HR (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Director of HR

**Role ID:** `RL-HR-80086`
**Department:** HR
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Purge CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Tweak Jira System Admin (Full Authorization Verified)
- Configure MongoDB User Data Store (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Revoke NetSuite ERP (Full Authorization Verified)
- Erase Salesforce CRM (Full Authorization Verified)
- Purge Azure Active Directory (Full Authorization Verified)
- Adjust AWS Admin Console (Full Authorization Verified)
- Manage Splunk Security Logs (Full Authorization Verified)
- Review records within HR Operations
- Audit records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Slack Enterprise Grid, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of HR needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of HR receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Director of HR (Platform)

**Role ID:** `RL-HR-80077`
**Department:** HR
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Modify Datadog APM (Full Authorization Verified)
- Destroy Salesforce CRM (Full Authorization Verified)
- Erase HubSpot Marketing (Full Authorization Verified)
- Edit Jira System Admin (Full Authorization Verified)
- Terminate Slack Enterprise Grid (Full Authorization Verified)
- Adjust GCP Core Infrastructure (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Drop Snowflake Data Warehouse (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Modify Zendesk Support Desk (Full Authorization Verified)
- Examine records within HR Operations
- Consult records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: Datadog APM, Salesforce CRM, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of HR (Platform) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of HR (Platform) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Director of HR (Analytics)

**Role ID:** `RL-HR-80061`
**Department:** HR
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Manage Figma Enterprise (Full Authorization Verified)
- Terminate Zendesk Support Desk (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Change Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Alter NetSuite ERP (Full Authorization Verified)
- Drop Workday HRIS (Full Authorization Verified)
- Erase CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Destroy Jira System Admin (Full Authorization Verified)
- Inspect records within HR Operations
- Audit records within HR Operations
- Read records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: Figma Enterprise, Zendesk Support Desk, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of HR (Analytics) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of HR (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Director of HR (Core)

**Role ID:** `RL-HR-80044`
**Department:** HR
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Remove NetSuite ERP (Full Authorization Verified)
- Destroy Jira System Admin (Full Authorization Verified)
- Delete Datadog APM (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Delete Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Remove AWS Admin Console (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Audit records within HR Operations
- Access records within HR Operations
- View records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), NetSuite ERP, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of HR (Core) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of HR (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Director of HR (North America)

**Role ID:** `RL-HR-80051`
**Department:** HR
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Destroy HubSpot Marketing (Full Authorization Verified)
- Erase Splunk Security Logs (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Destroy Snowflake Data Warehouse (Full Authorization Verified)
- Revoke MongoDB User Data Store (Full Authorization Verified)
- Erase Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View records within HR Operations
- Monitor records within HR Operations
- View records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and HR aggregate data.

#### Systems Access
Authorized platforms: HubSpot Marketing, Splunk Security Logs, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Director of HR (North America) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Director of HR (North America) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior HR Manager

**Role ID:** `RL-HR-70074`
**Department:** HR
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Azure Active Directory (Full Authorization Verified)
- Construct Jira System Admin (Full Authorization Verified)
- Setup Figma Enterprise (Full Authorization Verified)
- Initialize GCP Core Infrastructure (Full Authorization Verified)
- Initialize Snowflake Data Warehouse (Full Authorization Verified)
- Create MongoDB User Data Store (Full Authorization Verified)
- Setup Workday HRIS (Full Authorization Verified)
- Produce AWS Admin Console (Full Authorization Verified)
- Alter Zendesk Support Desk (Full Authorization Verified)
- Read records within HR Operations
- Audit records within HR Operations
- Inspect records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Jira System Admin, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior HR Manager needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior HR Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior HR Manager (Growth)

**Role ID:** `RL-HR-70073`
**Department:** HR
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Construct Kubernetes Production Cluster (Full Authorization Verified)
- Generate Workday HRIS (Full Authorization Verified)
- Setup GitHub Enterprise Admin (Full Authorization Verified)
- Construct NetSuite ERP (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Edit GCP Core Infrastructure (Full Authorization Verified)
- Construct Figma Enterprise (Full Authorization Verified)
- Setup CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect records within HR Operations
- Examine records within HR Operations
- Monitor records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Workday HRIS, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior HR Manager (Growth) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior HR Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior HR Manager (Cloud)

**Role ID:** `RL-HR-70068`
**Department:** HR
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Update Zendesk Support Desk (Full Authorization Verified)
- Alter AWS Admin Console (Full Authorization Verified)
- Produce Kubernetes Production Cluster (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Update Splunk Security Logs (Full Authorization Verified)
- Change Workday HRIS (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Update HubSpot Marketing (Full Authorization Verified)
- Initialize Snowflake Data Warehouse (Full Authorization Verified)
- Read records within HR Operations
- Consult records within HR Operations
- Consult records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, AWS Admin Console, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior HR Manager (Cloud) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior HR Manager (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior HR Manager (Analytics)

**Role ID:** `RL-HR-70051`
**Department:** HR
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Produce Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Setup NetSuite ERP (Full Authorization Verified)
- Adjust Zendesk Support Desk (Full Authorization Verified)
- Modify HubSpot Marketing (Full Authorization Verified)
- Construct Workday HRIS (Full Authorization Verified)
- Initialize Salesforce CRM (Full Authorization Verified)
- Modify Figma Enterprise (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Setup GitHub Enterprise Admin (Full Authorization Verified)
- Review records within HR Operations
- Inspect records within HR Operations
- Examine records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), NetSuite ERP, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior HR Manager (Analytics) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior HR Manager (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior HR Manager (Growth)

**Role ID:** `RL-HR-70068`
**Department:** HR
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Adjust CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Modify Zendesk Support Desk (Full Authorization Verified)
- Instantiate Azure Active Directory (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Tweak Workday HRIS (Full Authorization Verified)
- Construct Kubernetes Production Cluster (Full Authorization Verified)
- Instantiate Datadog APM (Full Authorization Verified)
- Initialize Snowflake Data Warehouse (Full Authorization Verified)
- Tweak Figma Enterprise (Full Authorization Verified)
- Inspect records within HR Operations
- Audit records within HR Operations
- Review records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), Zendesk Support Desk, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior HR Manager (Growth) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior HR Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### HR Manager

**Role ID:** `RL-HR-60088`
**Department:** HR
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Generate Snowflake Data Warehouse (Full Authorization Verified)
- Update AWS Admin Console (Full Authorization Verified)
- Alter Salesforce CRM (Full Authorization Verified)
- Produce HubSpot Marketing (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Change NetSuite ERP (Full Authorization Verified)
- Construct Figma Enterprise (Full Authorization Verified)
- Manage GitHub Enterprise Admin (Full Authorization Verified)
- Monitor records within HR Operations
- Read records within HR Operations
- Examine records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, AWS Admin Console, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A HR Manager needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The HR Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### HR Manager (Core)

**Role ID:** `RL-HR-60019`
**Department:** HR
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Create Zendesk Support Desk (Full Authorization Verified)
- Generate Datadog APM (Full Authorization Verified)
- Create Splunk Security Logs (Full Authorization Verified)
- Generate Snowflake Data Warehouse (Full Authorization Verified)
- Change Kubernetes Production Cluster (Full Authorization Verified)
- Build GitHub Enterprise Admin (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Produce Slack Enterprise Grid (Full Authorization Verified)
- Examine records within HR Operations
- Read records within HR Operations
- Monitor records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Datadog APM, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A HR Manager (Core) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The HR Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### HR Manager (Core)

**Role ID:** `RL-HR-60029`
**Department:** HR
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Change MongoDB User Data Store (Full Authorization Verified)
- Build Salesforce CRM (Full Authorization Verified)
- Edit AWS Admin Console (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Manage Splunk Security Logs (Full Authorization Verified)
- Create Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Produce Staging Environments (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Read records within HR Operations
- Monitor records within HR Operations
- Consult records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Salesforce CRM, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A HR Manager (Core) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The HR Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### HR Manager (Enterprise)

**Role ID:** `RL-HR-60079`
**Department:** HR
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Create Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Instantiate Azure Active Directory (Full Authorization Verified)
- Construct Figma Enterprise (Full Authorization Verified)
- Instantiate Splunk Security Logs (Full Authorization Verified)
- Setup Jira System Admin (Full Authorization Verified)
- Initialize Snowflake Data Warehouse (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Change CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Audit records within HR Operations
- Inspect records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Azure Active Directory, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A HR Manager (Enterprise) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The HR Manager (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### HR Manager (Infrastructure)

**Role ID:** `RL-HR-60083`
**Department:** HR
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust Zendesk Support Desk (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Instantiate NetSuite ERP (Full Authorization Verified)
- Tweak GCP Core Infrastructure (Full Authorization Verified)
- Generate Workday HRIS (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Instantiate Kubernetes Production Cluster (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Review records within HR Operations
- Review records within HR Operations
- Consult records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Staging Environments, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A HR Manager (Infrastructure) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The HR Manager (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Talent Acquisition Lead

**Role ID:** `RL-HR-50021`
**Department:** HR
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Setup Snowflake Data Warehouse (Full Authorization Verified)
- Adjust GitHub Enterprise Admin (Full Authorization Verified)
- Setup Figma Enterprise (Full Authorization Verified)
- Create Kubernetes Production Cluster (Full Authorization Verified)
- Setup Salesforce CRM (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Access records within HR Operations
- View records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, GitHub Enterprise Admin, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Talent Acquisition Lead needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Talent Acquisition Lead (Enterprise)

**Role ID:** `RL-HR-50022`
**Department:** HR
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Adjust HubSpot Marketing (Full Authorization Verified)
- Update CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Produce Kubernetes Production Cluster (Full Authorization Verified)
- Tweak Azure Active Directory (Full Authorization Verified)
- Setup Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Build GitHub Enterprise Admin (Full Authorization Verified)
- View records within HR Operations
- Monitor records within HR Operations
- Monitor records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, CI/CD Pipelines (Jenkins/GitHub Actions), GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Talent Acquisition Lead (Enterprise) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Talent Acquisition Lead (Analytics)

**Role ID:** `RL-HR-50022`
**Department:** HR
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Generate GitHub Enterprise Admin (Full Authorization Verified)
- Manage Workday HRIS (Full Authorization Verified)
- Tweak Jira System Admin (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Generate Salesforce CRM (Full Authorization Verified)
- Produce MongoDB User Data Store (Full Authorization Verified)
- Produce Slack Enterprise Grid (Full Authorization Verified)
- Consult records within HR Operations
- Access records within HR Operations
- Monitor records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Splunk Security Logs
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Workday HRIS, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Talent Acquisition Lead (Analytics) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Talent Acquisition Lead (Enterprise)

**Role ID:** `RL-HR-50098`
**Department:** HR
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Edit NetSuite ERP (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Change Jira System Admin (Full Authorization Verified)
- Adjust Azure Active Directory (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Adjust Datadog APM (Full Authorization Verified)
- Edit Figma Enterprise (Full Authorization Verified)
- Examine records within HR Operations
- Inspect records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: NetSuite ERP, MongoDB User Data Store, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Talent Acquisition Lead (Enterprise) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Talent Acquisition Lead (Infrastructure)

**Role ID:** `RL-HR-50054`
**Department:** HR
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Manage MongoDB User Data Store (Full Authorization Verified)
- Initialize Datadog APM (Full Authorization Verified)
- Generate Zendesk Support Desk (Full Authorization Verified)
- Construct Workday HRIS (Full Authorization Verified)
- Tweak Azure Active Directory (Full Authorization Verified)
- Change Splunk Security Logs (Full Authorization Verified)
- Setup AWS Admin Console (Full Authorization Verified)
- Review records within HR Operations
- View records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, Datadog APM, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Talent Acquisition Lead (Infrastructure) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior HR Business Partner

**Role ID:** `RL-HR-40058`
**Department:** HR
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Manage CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Tweak AWS Admin Console (Full Authorization Verified)
- Alter Kubernetes Production Cluster (Full Authorization Verified)
- Produce HubSpot Marketing (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Review records within HR Operations
- Review records within HR Operations
- Read records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, CI/CD Pipelines (Jenkins/GitHub Actions), AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior HR Business Partner needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior HR Business Partner (Enterprise)

**Role ID:** `RL-HR-40026`
**Department:** HR
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Build Salesforce CRM (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Setup Datadog APM (Full Authorization Verified)
- Tweak Jira System Admin (Full Authorization Verified)
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Review records within HR Operations
- Read records within HR Operations
- Inspect records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, AWS Admin Console, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior HR Business Partner (Enterprise) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior HR Business Partner (Platform)

**Role ID:** `RL-HR-40039`
**Department:** HR
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Modify MongoDB User Data Store (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- Modify Workday HRIS (Full Authorization Verified)
- Alter Zendesk Support Desk (Full Authorization Verified)
- Change HubSpot Marketing (Full Authorization Verified)
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Read records within HR Operations
- Audit records within HR Operations
- Consult records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, NetSuite ERP, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior HR Business Partner (Platform) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior HR Business Partner (Infrastructure)

**Role ID:** `RL-HR-40069`
**Department:** HR
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Initialize GitHub Enterprise Admin (Full Authorization Verified)
- Alter Salesforce CRM (Full Authorization Verified)
- Initialize Jira System Admin (Full Authorization Verified)
- Initialize GCP Core Infrastructure (Full Authorization Verified)
- Generate Azure Active Directory (Full Authorization Verified)
- Build HubSpot Marketing (Full Authorization Verified)
- View records within HR Operations
- View records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Salesforce CRM, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior HR Business Partner (Infrastructure) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior HR Business Partner (Platform)

**Role ID:** `RL-HR-40062`
**Department:** HR
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Produce Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Setup Figma Enterprise (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- Construct GitHub Enterprise Admin (Full Authorization Verified)
- Instantiate Snowflake Data Warehouse (Full Authorization Verified)
- Generate Azure Active Directory (Full Authorization Verified)
- Examine records within HR Operations
- Read records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Figma Enterprise, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior HR Business Partner (Platform) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### HR Generalist

**Role ID:** `RL-HR-30027`
**Department:** HR
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Azure Active Directory (Full Authorization Verified)
- Access HubSpot Marketing (Full Authorization Verified)
- View Workday HRIS (Full Authorization Verified)
- View Staging Environments (Full Authorization Verified)
- Review Kubernetes Production Cluster (Full Authorization Verified)
- Examine records within HR Operations
- Monitor records within HR Operations
- Read records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, HubSpot Marketing, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Generalist needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### HR Generalist (Cloud)

**Role ID:** `RL-HR-30066`
**Department:** HR
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect GitHub Enterprise Admin (Full Authorization Verified)
- Consult Staging Environments (Full Authorization Verified)
- Examine AWS Admin Console (Full Authorization Verified)
- View Datadog APM (Full Authorization Verified)
- Monitor Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Consult records within HR Operations
- Review records within HR Operations
- Examine records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Staging Environments, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Generalist (Cloud) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### HR Generalist (Infrastructure)

**Role ID:** `RL-HR-30046`
**Department:** HR
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Jira System Admin (Full Authorization Verified)
- Inspect Figma Enterprise (Full Authorization Verified)
- Monitor Staging Environments (Full Authorization Verified)
- Read Splunk Security Logs (Full Authorization Verified)
- Consult Azure Active Directory (Full Authorization Verified)
- Audit records within HR Operations
- Consult records within HR Operations
- View records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Figma Enterprise, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Generalist (Infrastructure) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### HR Generalist (North America)

**Role ID:** `RL-HR-30050`
**Department:** HR
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect HubSpot Marketing (Full Authorization Verified)
- Monitor Staging Environments (Full Authorization Verified)
- Access CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Audit Datadog APM (Full Authorization Verified)
- Inspect AWS Admin Console (Full Authorization Verified)
- Access records within HR Operations
- Review records within HR Operations
- Examine records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Staging Environments, CI/CD Pipelines (Jenkins/GitHub Actions)

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Generalist (North America) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### HR Generalist (APAC Region)

**Role ID:** `RL-HR-30060`
**Department:** HR
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View Staging Environments (Full Authorization Verified)
- View Slack Enterprise Grid (Full Authorization Verified)
- View Jira System Admin (Full Authorization Verified)
- View GCP Core Infrastructure (Full Authorization Verified)
- View Kubernetes Production Cluster (Full Authorization Verified)
- Read records within HR Operations
- Consult records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Slack Enterprise Grid, Jira System Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Generalist (APAC Region) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### HR Intern

**Role ID:** `RL-HR-10099`
**Department:** HR
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Salesforce CRM (Full Authorization Verified)
- Access AWS Admin Console (Full Authorization Verified)
- Inspect Slack Enterprise Grid (Full Authorization Verified)
- Monitor records within HR Operations
- Inspect records within HR Operations
- Examine records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, AWS Admin Console, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Intern needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### HR Intern (Platform)

**Role ID:** `RL-HR-10060`
**Department:** HR
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult Jira System Admin (Full Authorization Verified)
- Inspect HubSpot Marketing (Full Authorization Verified)
- Monitor Snowflake Data Warehouse (Full Authorization Verified)
- Read records within HR Operations
- Examine records within HR Operations
- View records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, HubSpot Marketing, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Intern (Platform) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### HR Intern (North America)

**Role ID:** `RL-HR-10010`
**Department:** HR
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Figma Enterprise (Full Authorization Verified)
- Consult Workday HRIS (Full Authorization Verified)
- Examine Slack Enterprise Grid (Full Authorization Verified)
- Read records within HR Operations
- View records within HR Operations
- Read records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Workday HRIS, Slack Enterprise Grid

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Intern (North America) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### HR Intern (Platform)

**Role ID:** `RL-HR-10024`
**Department:** HR
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor GitHub Enterprise Admin (Full Authorization Verified)
- Monitor HubSpot Marketing (Full Authorization Verified)
- Consult GCP Core Infrastructure (Full Authorization Verified)
- Access records within HR Operations
- Consult records within HR Operations
- Examine records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, HubSpot Marketing, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Intern (Platform) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### HR Intern (Analytics)

**Role ID:** `RL-HR-10016`
**Department:** HR
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Review Slack Enterprise Grid (Full Authorization Verified)
- Read Splunk Security Logs (Full Authorization Verified)
- Read Staging Environments (Full Authorization Verified)
- Consult records within HR Operations
- View records within HR Operations
- Read records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Splunk Security Logs, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A HR Intern (Analytics) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Recruiting Contractor

**Role ID:** `RL-HR-20094`
**Department:** HR
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Workday HRIS (Full Authorization Verified)
- Inspect Snowflake Data Warehouse (Full Authorization Verified)
- Audit Azure Active Directory (Full Authorization Verified)
- Access Splunk Security Logs (Full Authorization Verified)
- Audit records within HR Operations
- Access records within HR Operations
- Inspect records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Snowflake Data Warehouse, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Recruiting Contractor needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Recruiting Contractor (Growth)

**Role ID:** `RL-HR-20022`
**Department:** HR
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access HubSpot Marketing (Full Authorization Verified)
- Access Snowflake Data Warehouse (Full Authorization Verified)
- Review GCP Core Infrastructure (Full Authorization Verified)
- View MongoDB User Data Store (Full Authorization Verified)
- Audit records within HR Operations
- View records within HR Operations
- View records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Snowflake Data Warehouse, GCP Core Infrastructure

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Recruiting Contractor (Growth) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Recruiting Contractor (Analytics)

**Role ID:** `RL-HR-20014`
**Department:** HR
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Staging Environments (Full Authorization Verified)
- Consult Snowflake Data Warehouse (Full Authorization Verified)
- Examine Salesforce CRM (Full Authorization Verified)
- Examine MongoDB User Data Store (Full Authorization Verified)
- Inspect records within HR Operations
- Monitor records within HR Operations
- Access records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Snowflake Data Warehouse, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Recruiting Contractor (Analytics) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Recruiting Contractor (APAC Region)

**Role ID:** `RL-HR-20032`
**Department:** HR
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View GCP Core Infrastructure (Full Authorization Verified)
- Review Staging Environments (Full Authorization Verified)
- Audit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Consult Snowflake Data Warehouse (Full Authorization Verified)
- Review records within HR Operations
- Inspect records within HR Operations
- Examine records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, Staging Environments, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Recruiting Contractor (APAC Region) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Recruiting Contractor (Enterprise)

**Role ID:** `RL-HR-20065`
**Department:** HR
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult Figma Enterprise (Full Authorization Verified)
- Inspect Staging Environments (Full Authorization Verified)
- Monitor Zendesk Support Desk (Full Authorization Verified)
- Inspect Slack Enterprise Grid (Full Authorization Verified)
- Review records within HR Operations
- Review records within HR Operations
- Audit records within HR Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to HR team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Figma Enterprise, Staging Environments, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Recruiting Contractor (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

