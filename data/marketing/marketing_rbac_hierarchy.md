---
title: Marketing RBAC Hierarchy
department: marketing
role_access: marketing,employee,manager,admin,c-level
sensitivity: high
document_type: rbac_hierarchy
last_updated: 2026-03-03
version: 2.0
---

# Organization

## Marketing Department

The Marketing department follows a strict hierarchical Role-Based Access Control (RBAC) model. Access is granted on the principle of least privilege, requiring continuous validation through our identity providers and multi-factor authentication systems.

### Chief Marketing Officer (CMO)

**Role ID:** `RL-MAR-100038`
**Department:** Marketing
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Adjust AWS Admin Console (Full Authorization Verified)
- Delete Datadog APM (Full Authorization Verified)
- Configure Slack Enterprise Grid (Full Authorization Verified)
- Change Zendesk Support Desk (Full Authorization Verified)
- Tweak MongoDB User Data Store (Full Authorization Verified)
- Remove Splunk Security Logs (Full Authorization Verified)
- Modify GCP Core Infrastructure (Full Authorization Verified)
- Configure Staging Environments (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Access records within Marketing Operations
- Inspect records within Marketing Operations
- Access records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Jira System Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), AWS Admin Console, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Marketing Officer (CMO) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Marketing Officer (CMO) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Marketing Officer (CMO) (Compliance)

**Role ID:** `RL-MAR-100069`
**Department:** Marketing
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Modify Zendesk Support Desk (Full Authorization Verified)
- Alter CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit Datadog APM (Full Authorization Verified)
- Remove Jira System Admin (Full Authorization Verified)
- Adjust Workday HRIS (Full Authorization Verified)
- Revoke HubSpot Marketing (Full Authorization Verified)
- Modify Azure Active Directory (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Alter Splunk Security Logs (Full Authorization Verified)
- Terminate AWS Admin Console (Full Authorization Verified)
- Consult records within Marketing Operations
- Access records within Marketing Operations
- Consult records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Slack Enterprise Grid

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, MongoDB User Data Store, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Marketing Officer (CMO) (Compliance) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Marketing Officer (CMO) (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Chief Marketing Officer (CMO) (Cloud)

**Role ID:** `RL-MAR-100064`
**Department:** Marketing
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Edit Slack Enterprise Grid (Full Authorization Verified)
- Configure Workday HRIS (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Destroy Datadog APM (Full Authorization Verified)
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Configure Snowflake Data Warehouse (Full Authorization Verified)
- Terminate MongoDB User Data Store (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Manage Staging Environments (Full Authorization Verified)
- Erase NetSuite ERP (Full Authorization Verified)
- Drop Jira System Admin (Full Authorization Verified)
- Read records within Marketing Operations
- Read records within Marketing Operations
- Examine records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Splunk Security Logs

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Workday HRIS, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Marketing Officer (CMO) (Cloud) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Marketing Officer (CMO) (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Chief Marketing Officer (CMO) (Analytics)

**Role ID:** `RL-MAR-100021`
**Department:** Marketing
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Purge Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Alter Jira System Admin (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Erase Figma Enterprise (Full Authorization Verified)
- Destroy Staging Environments (Full Authorization Verified)
- Revoke Datadog APM (Full Authorization Verified)
- Manage MongoDB User Data Store (Full Authorization Verified)
- Update NetSuite ERP (Full Authorization Verified)
- Terminate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Configure GCP Core Infrastructure (Full Authorization Verified)
- Delete Kubernetes Production Cluster (Full Authorization Verified)
- Delete Salesforce CRM (Full Authorization Verified)
- Review records within Marketing Operations
- View records within Marketing Operations
- Review records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing AWS Admin Console

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Jira System Admin, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Marketing Officer (CMO) (Analytics) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Marketing Officer (CMO) (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Chief Marketing Officer (CMO) (Analytics)

**Role ID:** `RL-MAR-100075`
**Department:** Marketing
**Reporting To:** Board of Directors
**Access Level:** 10/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Manage AWS Admin Console (Full Authorization Verified)
- Manage Slack Enterprise Grid (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Tweak Jira System Admin (Full Authorization Verified)
- Manage NetSuite ERP (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Drop GitHub Enterprise Admin (Full Authorization Verified)
- Update Snowflake Data Warehouse (Full Authorization Verified)
- Manage CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Destroy Splunk Security Logs (Full Authorization Verified)
- Erase HubSpot Marketing (Full Authorization Verified)
- Access records within Marketing Operations
- Examine records within Marketing Operations
- Audit records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Figma Enterprise

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, Slack Enterprise Grid, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Board of Directors.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Chief Marketing Officer (CMO) (Analytics) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Chief Marketing Officer (CMO) (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### VP of Marketing

**Role ID:** `RL-MAR-90080`
**Department:** Marketing
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Alter AWS Admin Console (Full Authorization Verified)
- Remove Staging Environments (Full Authorization Verified)
- Modify Workday HRIS (Full Authorization Verified)
- Manage Kubernetes Production Cluster (Full Authorization Verified)
- Modify GitHub Enterprise Admin (Full Authorization Verified)
- Tweak Datadog APM (Full Authorization Verified)
- Erase Azure Active Directory (Full Authorization Verified)
- Configure Splunk Security Logs (Full Authorization Verified)
- Configure Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Modify Jira System Admin (Full Authorization Verified)
- Revoke Slack Enterprise Grid (Full Authorization Verified)
- Inspect records within Marketing Operations
- Review records within Marketing Operations
- Audit records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing NetSuite ERP

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, Staging Environments, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Marketing needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Marketing receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### VP of Marketing (Analytics)

**Role ID:** `RL-MAR-90081`
**Department:** Marketing
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Purge Workday HRIS (Full Authorization Verified)
- Destroy MongoDB User Data Store (Full Authorization Verified)
- Delete Zendesk Support Desk (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Drop Datadog APM (Full Authorization Verified)
- Terminate AWS Admin Console (Full Authorization Verified)
- Update Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit Salesforce CRM (Full Authorization Verified)
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Edit Azure Active Directory (Full Authorization Verified)
- Modify Jira System Admin (Full Authorization Verified)
- Access records within Marketing Operations
- Access records within Marketing Operations
- Audit records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing HubSpot Marketing

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: Workday HRIS, MongoDB User Data Store, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Marketing (Analytics) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Marketing (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### VP of Marketing (Analytics)

**Role ID:** `RL-MAR-90077`
**Department:** Marketing
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Erase NetSuite ERP (Full Authorization Verified)
- Tweak MongoDB User Data Store (Full Authorization Verified)
- Delete HubSpot Marketing (Full Authorization Verified)
- Purge Datadog APM (Full Authorization Verified)
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Update Figma Enterprise (Full Authorization Verified)
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Terminate Slack Enterprise Grid (Full Authorization Verified)
- Purge Workday HRIS (Full Authorization Verified)
- Configure Salesforce CRM (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- View records within Marketing Operations
- Access records within Marketing Operations
- View records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Zendesk Support Desk

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: NetSuite ERP, MongoDB User Data Store, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Marketing (Analytics) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Marketing (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### VP of Marketing (Enterprise)

**Role ID:** `RL-MAR-90026`
**Department:** Marketing
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Manage Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Terminate Slack Enterprise Grid (Full Authorization Verified)
- Alter Azure Active Directory (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Configure Datadog APM (Full Authorization Verified)
- Destroy Snowflake Data Warehouse (Full Authorization Verified)
- Manage GCP Core Infrastructure (Full Authorization Verified)
- Manage Salesforce CRM (Full Authorization Verified)
- Terminate HubSpot Marketing (Full Authorization Verified)
- Drop Kubernetes Production Cluster (Full Authorization Verified)
- Destroy CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Monitor records within Marketing Operations
- Examine records within Marketing Operations
- Inspect records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Jira System Admin

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Slack Enterprise Grid, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Marketing (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Marketing (Enterprise) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### VP of Marketing (EMEA Region)

**Role ID:** `RL-MAR-90044`
**Department:** Marketing
**Reporting To:** C-Level Executive (e.g., CEO, CTO)
**Access Level:** 9/10
**Audit Log Level:** High
**Security Classification Level:** Top Secret

#### Permissions
- Terminate AWS Admin Console (Full Authorization Verified)
- Alter GitHub Enterprise Admin (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Delete Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Alter NetSuite ERP (Full Authorization Verified)
- Erase Slack Enterprise Grid (Full Authorization Verified)
- Adjust Snowflake Data Warehouse (Full Authorization Verified)
- Configure Figma Enterprise (Full Authorization Verified)
- Erase Jira System Admin (Full Authorization Verified)
- Monitor records within Marketing Operations
- Monitor records within Marketing Operations
- Monitor records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, GitHub Enterprise Admin, Workday HRIS

#### Escalation Rules
- Any unhandled operational block must be escalated to C-Level Executive (e.g., CEO, CTO).

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A VP of Marketing (EMEA Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The VP of Marketing (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Marketing Director

**Role ID:** `RL-MAR-80059`
**Department:** Marketing
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Revoke Staging Environments (Full Authorization Verified)
- Purge Zendesk Support Desk (Full Authorization Verified)
- Purge Salesforce CRM (Full Authorization Verified)
- Remove Splunk Security Logs (Full Authorization Verified)
- Tweak Jira System Admin (Full Authorization Verified)
- Adjust Figma Enterprise (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Purge Snowflake Data Warehouse (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- View records within Marketing Operations
- Consult records within Marketing Operations
- Read records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), Staging Environments, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Marketing Director needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Director receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Marketing Director (Analytics)

**Role ID:** `RL-MAR-80027`
**Department:** Marketing
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Drop AWS Admin Console (Full Authorization Verified)
- Change Staging Environments (Full Authorization Verified)
- Terminate Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Change Jira System Admin (Full Authorization Verified)
- Erase GCP Core Infrastructure (Full Authorization Verified)
- Terminate Figma Enterprise (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Remove GitHub Enterprise Admin (Full Authorization Verified)
- Revoke Datadog APM (Full Authorization Verified)
- Delete Workday HRIS (Full Authorization Verified)
- Monitor records within Marketing Operations
- Examine records within Marketing Operations
- Read records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: AWS Admin Console, Staging Environments, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Marketing Director (Analytics) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Director (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Marketing Director (Cloud)

**Role ID:** `RL-MAR-80014`
**Department:** Marketing
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Remove Slack Enterprise Grid (Full Authorization Verified)
- Remove CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Delete Salesforce CRM (Full Authorization Verified)
- Change AWS Admin Console (Full Authorization Verified)
- Adjust Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Revoke Jira System Admin (Full Authorization Verified)
- Alter Workday HRIS (Full Authorization Verified)
- Purge Staging Environments (Full Authorization Verified)
- Tweak GitHub Enterprise Admin (Full Authorization Verified)
- Manage Kubernetes Production Cluster (Full Authorization Verified)
- Review records within Marketing Operations
- Examine records within Marketing Operations
- Read records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, CI/CD Pipelines (Jenkins/GitHub Actions), Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Marketing Director (Cloud) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Director (Cloud) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Marketing Director (Analytics)

**Role ID:** `RL-MAR-80025`
**Department:** Marketing
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Modify Zendesk Support Desk (Full Authorization Verified)
- Drop HubSpot Marketing (Full Authorization Verified)
- Drop Splunk Security Logs (Full Authorization Verified)
- Modify Snowflake Data Warehouse (Full Authorization Verified)
- Modify Figma Enterprise (Full Authorization Verified)
- Edit Jira System Admin (Full Authorization Verified)
- Update Workday HRIS (Full Authorization Verified)
- Delete Slack Enterprise Grid (Full Authorization Verified)
- Drop Staging Environments (Full Authorization Verified)
- Terminate Datadog APM (Full Authorization Verified)
- Monitor records within Marketing Operations
- Audit records within Marketing Operations
- Examine records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing GitHub Enterprise Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: Zendesk Support Desk, HubSpot Marketing, Splunk Security Logs

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Marketing Director (Analytics) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Director (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Marketing Director (Compliance)

**Role ID:** `RL-MAR-80014`
**Department:** Marketing
**Reporting To:** Vice President of Department
**Access Level:** 8/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Change Azure Active Directory (Full Authorization Verified)
- Remove Figma Enterprise (Full Authorization Verified)
- Delete Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Terminate Splunk Security Logs (Full Authorization Verified)
- Revoke Kubernetes Production Cluster (Full Authorization Verified)
- Terminate MongoDB User Data Store (Full Authorization Verified)
- Terminate Workday HRIS (Full Authorization Verified)
- Modify Slack Enterprise Grid (Full Authorization Verified)
- Configure NetSuite ERP (Full Authorization Verified)
- Read records within Marketing Operations
- Access records within Marketing Operations
- Read records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Global Data Scope: Inter-departmental metrics and Marketing aggregate data.

#### Systems Access
Authorized platforms: Snowflake Data Warehouse, Azure Active Directory, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Vice President of Department.

#### Approval Authority
- Can approve budgets up to $500,000 without board intervention.
- Can authorize system-wide architecture changes.

#### Example Use Cases
- **Scenario 1:** A Marketing Director (Compliance) needs to monitor quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Director (Compliance) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Senior Marketing Manager

**Role ID:** `RL-MAR-70098`
**Department:** Marketing
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Create Jira System Admin (Full Authorization Verified)
- Configure HubSpot Marketing (Full Authorization Verified)
- Configure Staging Environments (Full Authorization Verified)
- Modify CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit AWS Admin Console (Full Authorization Verified)
- Modify Figma Enterprise (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Create Kubernetes Production Cluster (Full Authorization Verified)
- Produce Azure Active Directory (Full Authorization Verified)
- Read records within Marketing Operations
- Examine records within Marketing Operations
- Monitor records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, HubSpot Marketing, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Manager needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Marketing Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Senior Marketing Manager (Analytics)

**Role ID:** `RL-MAR-70095`
**Department:** Marketing
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Workday HRIS (Full Authorization Verified)
- Modify MongoDB User Data Store (Full Authorization Verified)
- Update AWS Admin Console (Full Authorization Verified)
- Create CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Update Zendesk Support Desk (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Setup Snowflake Data Warehouse (Full Authorization Verified)
- Construct Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Consult records within Marketing Operations
- Examine records within Marketing Operations
- View records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, MongoDB User Data Store, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Manager (Analytics) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Marketing Manager (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Marketing Manager (Infrastructure)

**Role ID:** `RL-MAR-70096`
**Department:** Marketing
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Configure GitHub Enterprise Admin (Full Authorization Verified)
- Modify Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Adjust HubSpot Marketing (Full Authorization Verified)
- Tweak Slack Enterprise Grid (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Tweak Staging Environments (Full Authorization Verified)
- Manage Workday HRIS (Full Authorization Verified)
- Produce MongoDB User Data Store (Full Authorization Verified)
- Setup CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Access records within Marketing Operations
- Audit records within Marketing Operations
- Access records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Production Database Cluster (PostgreSQL), HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Manager (Infrastructure) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Marketing Manager (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Senior Marketing Manager (EMEA Region)

**Role ID:** `RL-MAR-70037`
**Department:** Marketing
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Edit Slack Enterprise Grid (Full Authorization Verified)
- Generate Figma Enterprise (Full Authorization Verified)
- Manage Datadog APM (Full Authorization Verified)
- Construct HubSpot Marketing (Full Authorization Verified)
- Setup NetSuite ERP (Full Authorization Verified)
- Modify Splunk Security Logs (Full Authorization Verified)
- Tweak AWS Admin Console (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Access records within Marketing Operations
- Access records within Marketing Operations
- Read records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Azure Active Directory
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, Figma Enterprise, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Manager (EMEA Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Marketing Manager (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Senior Marketing Manager (Growth)

**Role ID:** `RL-MAR-70018`
**Department:** Marketing
**Reporting To:** Director of Department
**Access Level:** 7/10
**Audit Log Level:** High
**Security Classification Level:** Confidential

#### Permissions
- Modify AWS Admin Console (Full Authorization Verified)
- Manage Snowflake Data Warehouse (Full Authorization Verified)
- Setup Zendesk Support Desk (Full Authorization Verified)
- Instantiate Azure Active Directory (Full Authorization Verified)
- Modify NetSuite ERP (Full Authorization Verified)
- Initialize Salesforce CRM (Full Authorization Verified)
- Manage CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Edit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Setup GitHub Enterprise Admin (Full Authorization Verified)
- Consult records within Marketing Operations
- Audit records within Marketing Operations
- Review records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Snowflake Data Warehouse, Zendesk Support Desk

#### Escalation Rules
- Any unhandled operational block must be escalated to Director of Department.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Manager (Growth) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Senior Marketing Manager (Growth) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Partial read-ability into Finance and Strategy documents.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Marketing Manager

**Role ID:** `RL-MAR-60080`
**Department:** Marketing
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Edit AWS Admin Console (Full Authorization Verified)
- Create Staging Environments (Full Authorization Verified)
- Produce Azure Active Directory (Full Authorization Verified)
- Construct Splunk Security Logs (Full Authorization Verified)
- Edit NetSuite ERP (Full Authorization Verified)
- Change Datadog APM (Full Authorization Verified)
- Setup GitHub Enterprise Admin (Full Authorization Verified)
- Produce GCP Core Infrastructure (Full Authorization Verified)
- Inspect records within Marketing Operations
- Access records within Marketing Operations
- Consult records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing HubSpot Marketing
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Staging Environments, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Manager needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Manager receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Marketing Manager (Core)

**Role ID:** `RL-MAR-60059`
**Department:** Marketing
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Change Zendesk Support Desk (Full Authorization Verified)
- Edit Figma Enterprise (Full Authorization Verified)
- Initialize Datadog APM (Full Authorization Verified)
- Construct GCP Core Infrastructure (Full Authorization Verified)
- Build Staging Environments (Full Authorization Verified)
- Edit Workday HRIS (Full Authorization Verified)
- Update Splunk Security Logs (Full Authorization Verified)
- Build Azure Active Directory (Full Authorization Verified)
- Monitor records within Marketing Operations
- Inspect records within Marketing Operations
- Review records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Zendesk Support Desk, Figma Enterprise, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Manager (Core) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Manager (Core) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Marketing Manager (Analytics)

**Role ID:** `RL-MAR-60086`
**Department:** Marketing
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Update HubSpot Marketing (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Initialize AWS Admin Console (Full Authorization Verified)
- Tweak Splunk Security Logs (Full Authorization Verified)
- Update Staging Environments (Full Authorization Verified)
- Alter Snowflake Data Warehouse (Full Authorization Verified)
- Edit Figma Enterprise (Full Authorization Verified)
- Setup Azure Active Directory (Full Authorization Verified)
- Review records within Marketing Operations
- Monitor records within Marketing Operations
- Audit records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Salesforce CRM, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Manager (Analytics) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Manager (Analytics) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Marketing Manager (EMEA Region)

**Role ID:** `RL-MAR-60078`
**Department:** Marketing
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Update Jira System Admin (Full Authorization Verified)
- Update Salesforce CRM (Full Authorization Verified)
- Configure AWS Admin Console (Full Authorization Verified)
- Produce Figma Enterprise (Full Authorization Verified)
- Alter GCP Core Infrastructure (Full Authorization Verified)
- Edit Slack Enterprise Grid (Full Authorization Verified)
- Instantiate MongoDB User Data Store (Full Authorization Verified)
- Build Azure Active Directory (Full Authorization Verified)
- View records within Marketing Operations
- Read records within Marketing Operations
- Access records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Staging Environments
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Salesforce CRM, AWS Admin Console

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Manager (EMEA Region) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Manager (EMEA Region) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Marketing Manager (Infrastructure)

**Role ID:** `RL-MAR-60053`
**Department:** Marketing
**Reporting To:** Senior Manager
**Access Level:** 6/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Change Azure Active Directory (Full Authorization Verified)
- Initialize Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Instantiate Salesforce CRM (Full Authorization Verified)
- Create Figma Enterprise (Full Authorization Verified)
- Generate AWS Admin Console (Full Authorization Verified)
- Initialize Jira System Admin (Full Authorization Verified)
- Construct Splunk Security Logs (Full Authorization Verified)
- Instantiate MongoDB User Data Store (Full Authorization Verified)
- View records within Marketing Operations
- Inspect records within Marketing Operations
- View records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Production Database Cluster (PostgreSQL), Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Manager (Infrastructure) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.
- **Scenario 2:** Approving an emergency update. The Marketing Manager (Infrastructure) receives an alert, verifies the CI/CD pipeline, and clicks "Approve" to push to production.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Marketing Lead

**Role ID:** `RL-MAR-50049`
**Department:** Marketing
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Edit GitHub Enterprise Admin (Full Authorization Verified)
- Setup Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Create MongoDB User Data Store (Full Authorization Verified)
- Adjust NetSuite ERP (Full Authorization Verified)
- Generate GCP Core Infrastructure (Full Authorization Verified)
- Alter AWS Admin Console (Full Authorization Verified)
- Configure CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect records within Marketing Operations
- Read records within Marketing Operations
- View records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Datadog APM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Production Database Cluster (PostgreSQL), MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Lead needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Marketing Lead (EMEA Region)

**Role ID:** `RL-MAR-50039`
**Department:** Marketing
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Construct HubSpot Marketing (Full Authorization Verified)
- Adjust Azure Active Directory (Full Authorization Verified)
- Create Figma Enterprise (Full Authorization Verified)
- Modify AWS Admin Console (Full Authorization Verified)
- Build GitHub Enterprise Admin (Full Authorization Verified)
- Modify Jira System Admin (Full Authorization Verified)
- Read records within Marketing Operations
- Examine records within Marketing Operations
- Monitor records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Production Database Cluster (PostgreSQL), HubSpot Marketing, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Lead (EMEA Region) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Marketing Lead (Growth)

**Role ID:** `RL-MAR-50060`
**Department:** Marketing
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Update Azure Active Directory (Full Authorization Verified)
- Alter Datadog APM (Full Authorization Verified)
- Manage Splunk Security Logs (Full Authorization Verified)
- Alter Figma Enterprise (Full Authorization Verified)
- Configure Jira System Admin (Full Authorization Verified)
- Edit Snowflake Data Warehouse (Full Authorization Verified)
- View records within Marketing Operations
- Monitor records within Marketing Operations
- Access records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Kubernetes Production Cluster, Azure Active Directory, Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Lead (Growth) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Marketing Lead (Compliance)

**Role ID:** `RL-MAR-50027`
**Department:** Marketing
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Initialize Jira System Admin (Full Authorization Verified)
- Generate Staging Environments (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Change Workday HRIS (Full Authorization Verified)
- Create GitHub Enterprise Admin (Full Authorization Verified)
- Configure Kubernetes Production Cluster (Full Authorization Verified)
- Initialize Slack Enterprise Grid (Full Authorization Verified)
- Consult records within Marketing Operations
- Audit records within Marketing Operations
- Consult records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing CI/CD Pipelines (Jenkins/GitHub Actions)
- Strictly forbidden from accessing Azure Active Directory
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Staging Environments, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Lead (Compliance) needs to read quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Marketing Lead (Core)

**Role ID:** `RL-MAR-50087`
**Department:** Marketing
**Reporting To:** Manager
**Access Level:** 5/10
**Audit Log Level:** Medium
**Security Classification Level:** Confidential

#### Permissions
- Edit Staging Environments (Full Authorization Verified)
- Create NetSuite ERP (Full Authorization Verified)
- Construct MongoDB User Data Store (Full Authorization Verified)
- Initialize Slack Enterprise Grid (Full Authorization Verified)
- Edit HubSpot Marketing (Full Authorization Verified)
- Create GCP Core Infrastructure (Full Authorization Verified)
- Build Jira System Admin (Full Authorization Verified)
- Access records within Marketing Operations
- Inspect records within Marketing Operations
- Monitor records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing AWS Admin Console
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, NetSuite ERP, MongoDB User Data Store

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager.

#### Approval Authority
- Can approve team expenses up to $5,000.
- Can approve merge requests and production deployments.

#### Example Use Cases
- **Scenario 1:** A Marketing Lead (Core) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Marketing Specialist

**Role ID:** `RL-MAR-40046`
**Department:** Marketing
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Edit AWS Admin Console (Full Authorization Verified)
- Update Zendesk Support Desk (Full Authorization Verified)
- Edit Figma Enterprise (Full Authorization Verified)
- Alter Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Edit Datadog APM (Full Authorization Verified)
- Build Workday HRIS (Full Authorization Verified)
- Consult records within Marketing Operations
- Read records within Marketing Operations
- Read records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: AWS Admin Console, Zendesk Support Desk, Figma Enterprise

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Specialist needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Marketing Specialist (North America)

**Role ID:** `RL-MAR-40098`
**Department:** Marketing
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Construct Salesforce CRM (Full Authorization Verified)
- Instantiate NetSuite ERP (Full Authorization Verified)
- Produce Snowflake Data Warehouse (Full Authorization Verified)
- Construct HubSpot Marketing (Full Authorization Verified)
- Alter MongoDB User Data Store (Full Authorization Verified)
- Construct GCP Core Infrastructure (Full Authorization Verified)
- Consult records within Marketing Operations
- Access records within Marketing Operations
- Inspect records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Salesforce CRM, NetSuite ERP, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Specialist (North America) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot change permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Senior Marketing Specialist (Analytics)

**Role ID:** `RL-MAR-40048`
**Department:** Marketing
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Setup Datadog APM (Full Authorization Verified)
- Tweak CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Build Snowflake Data Warehouse (Full Authorization Verified)
- Adjust Splunk Security Logs (Full Authorization Verified)
- Setup Slack Enterprise Grid (Full Authorization Verified)
- Adjust Jira System Admin (Full Authorization Verified)
- Access records within Marketing Operations
- Monitor records within Marketing Operations
- Read records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Datadog APM, CI/CD Pipelines (Jenkins/GitHub Actions), Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Specialist (Analytics) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Acquisition integration: Temporary cross-domain identity mapping active for 90 days.

---

### Senior Marketing Specialist (North America)

**Role ID:** `RL-MAR-40043`
**Department:** Marketing
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Build Staging Environments (Full Authorization Verified)
- Adjust Kubernetes Production Cluster (Full Authorization Verified)
- Generate HubSpot Marketing (Full Authorization Verified)
- Construct NetSuite ERP (Full Authorization Verified)
- Initialize Zendesk Support Desk (Full Authorization Verified)
- Initialize MongoDB User Data Store (Full Authorization Verified)
- Inspect records within Marketing Operations
- Read records within Marketing Operations
- Read records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Kubernetes Production Cluster, HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Specialist (North America) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Senior Marketing Specialist (Infrastructure)

**Role ID:** `RL-MAR-40063`
**Department:** Marketing
**Reporting To:** Team Lead
**Access Level:** 4/10
**Audit Log Level:** Medium
**Security Classification Level:** Internal Use Only

#### Permissions
- Tweak Azure Active Directory (Full Authorization Verified)
- Tweak Kubernetes Production Cluster (Full Authorization Verified)
- Adjust Salesforce CRM (Full Authorization Verified)
- Instantiate NetSuite ERP (Full Authorization Verified)
- Instantiate CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Generate MongoDB User Data Store (Full Authorization Verified)
- Inspect records within Marketing Operations
- Review records within Marketing Operations
- Review records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing Figma Enterprise
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, Kubernetes Production Cluster, Salesforce CRM

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Senior Marketing Specialist (Infrastructure) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to erase audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Marketing Specialist

**Role ID:** `RL-MAR-30046`
**Department:** Marketing
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect Staging Environments (Full Authorization Verified)
- Inspect Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View NetSuite ERP (Full Authorization Verified)
- Examine CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect GCP Core Infrastructure (Full Authorization Verified)
- Inspect records within Marketing Operations
- Access records within Marketing Operations
- Consult records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Production Database Cluster (PostgreSQL), NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Specialist needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to revoke audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Marketing Specialist (Analytics)

**Role ID:** `RL-MAR-30028`
**Department:** Marketing
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect HubSpot Marketing (Full Authorization Verified)
- Monitor Datadog APM (Full Authorization Verified)
- Inspect GitHub Enterprise Admin (Full Authorization Verified)
- Monitor GCP Core Infrastructure (Full Authorization Verified)
- Audit NetSuite ERP (Full Authorization Verified)
- Monitor records within Marketing Operations
- Examine records within Marketing Operations
- Audit records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Slack Enterprise Grid
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Zendesk Support Desk
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Datadog APM, GitHub Enterprise Admin

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Specialist (Analytics) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to delete audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Marketing Specialist (North America)

**Role ID:** `RL-MAR-30043`
**Department:** Marketing
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read Jira System Admin (Full Authorization Verified)
- Audit HubSpot Marketing (Full Authorization Verified)
- Examine Staging Environments (Full Authorization Verified)
- Access CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- View AWS Admin Console (Full Authorization Verified)
- View records within Marketing Operations
- Access records within Marketing Operations
- Examine records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Splunk Security Logs
- Strictly forbidden from accessing GitHub Enterprise Admin
- Strictly forbidden from accessing MongoDB User Data Store
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, HubSpot Marketing, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Specialist (North America) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Marketing Specialist (Enterprise)

**Role ID:** `RL-MAR-30023`
**Department:** Marketing
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- View MongoDB User Data Store (Full Authorization Verified)
- View CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Inspect Snowflake Data Warehouse (Full Authorization Verified)
- Consult GitHub Enterprise Admin (Full Authorization Verified)
- Read Splunk Security Logs (Full Authorization Verified)
- View records within Marketing Operations
- Examine records within Marketing Operations
- Audit records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Datadog APM
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: MongoDB User Data Store, CI/CD Pipelines (Jenkins/GitHub Actions), Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Specialist (Enterprise) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot alter permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Role transfer in progress: Retains previous access for 14 days during overlap period.

---

### Marketing Specialist (Analytics)

**Role ID:** `RL-MAR-30062`
**Department:** Marketing
**Reporting To:** Team Lead or Manager
**Access Level:** 3/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Splunk Security Logs (Full Authorization Verified)
- Examine Salesforce CRM (Full Authorization Verified)
- Audit Kubernetes Production Cluster (Full Authorization Verified)
- View Datadog APM (Full Authorization Verified)
- View Figma Enterprise (Full Authorization Verified)
- Examine records within Marketing Operations
- Inspect records within Marketing Operations
- Inspect records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Zendesk Support Desk
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing NetSuite ERP
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Splunk Security Logs, Salesforce CRM, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Team Lead or Manager.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Specialist (Analytics) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- System maintenance window access bypassing standard IP restrictions.

---

### Marketing Intern

**Role ID:** `RL-MAR-10012`
**Department:** Marketing
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Examine Azure Active Directory (Full Authorization Verified)
- Read HubSpot Marketing (Full Authorization Verified)
- Access Kubernetes Production Cluster (Full Authorization Verified)
- Consult records within Marketing Operations
- Inspect records within Marketing Operations
- Monitor records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Jira System Admin
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Azure Active Directory, HubSpot Marketing, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Intern needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Marketing Intern (EMEA Region)

**Role ID:** `RL-MAR-10069`
**Department:** Marketing
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Read HubSpot Marketing (Full Authorization Verified)
- Monitor Salesforce CRM (Full Authorization Verified)
- Audit Staging Environments (Full Authorization Verified)
- Audit records within Marketing Operations
- Access records within Marketing Operations
- Examine records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing GCP Core Infrastructure
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: HubSpot Marketing, Salesforce CRM, Staging Environments

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Intern (EMEA Region) needs to inspect quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to destroy audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Marketing Intern (Core)

**Role ID:** `RL-MAR-10061`
**Department:** Marketing
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Workday HRIS (Full Authorization Verified)
- View Splunk Security Logs (Full Authorization Verified)
- Read Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- Review records within Marketing Operations
- Read records within Marketing Operations
- Examine records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing NetSuite ERP
- Strictly forbidden from accessing Kubernetes Production Cluster
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Workday HRIS, Splunk Security Logs, Production Database Cluster (PostgreSQL)

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Intern (Core) needs to audit quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to drop audit logs will trigger an immediate P0 security alert.
- Cannot configure permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Marketing Intern (APAC Region)

**Role ID:** `RL-MAR-10042`
**Department:** Marketing
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Consult Jira System Admin (Full Authorization Verified)
- Access GCP Core Infrastructure (Full Authorization Verified)
- Review Kubernetes Production Cluster (Full Authorization Verified)
- Access records within Marketing Operations
- Audit records within Marketing Operations
- Examine records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing HubSpot Marketing
- Strictly forbidden from accessing Staging Environments
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, GCP Core Infrastructure, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Intern (APAC Region) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot modify permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Temporary access elevation granted via ServiceNow JIRA ticket approved by VP.

---

### Marketing Intern (Enterprise)

**Role ID:** `RL-MAR-10073`
**Department:** Marketing
**Reporting To:** Senior Employee or Team Lead
**Access Level:** 1/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Staging Environments (Full Authorization Verified)
- Inspect Splunk Security Logs (Full Authorization Verified)
- Consult NetSuite ERP (Full Authorization Verified)
- Inspect records within Marketing Operations
- Audit records within Marketing Operations
- Examine records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Slack Enterprise Grid
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Staging Environments, Splunk Security Logs, NetSuite ERP

#### Escalation Rules
- Any unhandled operational block must be escalated to Senior Employee or Team Lead.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Intern (Enterprise) needs to examine quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

### Marketing Contractor

**Role ID:** `RL-MAR-20062`
**Department:** Marketing
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect CI/CD Pipelines (Jenkins/GitHub Actions) (Full Authorization Verified)
- Audit NetSuite ERP (Full Authorization Verified)
- Monitor Azure Active Directory (Full Authorization Verified)
- Inspect AWS Admin Console (Full Authorization Verified)
- Audit records within Marketing Operations
- Consult records within Marketing Operations
- View records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Snowflake Data Warehouse
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Kubernetes Production Cluster
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: CI/CD Pipelines (Jenkins/GitHub Actions), NetSuite ERP, Azure Active Directory

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Contractor needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot adjust permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Marketing Contractor (Analytics)

**Role ID:** `RL-MAR-20050`
**Department:** Marketing
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Inspect GitHub Enterprise Admin (Full Authorization Verified)
- Consult Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View Datadog APM (Full Authorization Verified)
- Consult GCP Core Infrastructure (Full Authorization Verified)
- Review records within Marketing Operations
- Read records within Marketing Operations
- Audit records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing AWS Admin Console
- Strictly forbidden from accessing MongoDB User Data Store
- Strictly forbidden from accessing Salesforce CRM
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GitHub Enterprise Admin, Production Database Cluster (PostgreSQL), Datadog APM

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Contractor (Analytics) needs to view quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot edit permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Third-party audit mode: Read-only access to all compliance logs but strictly prevented from state-modifying POST/PUT requests.

---

### Marketing Contractor (Compliance)

**Role ID:** `RL-MAR-20013`
**Department:** Marketing
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Audit GCP Core Infrastructure (Full Authorization Verified)
- Consult NetSuite ERP (Full Authorization Verified)
- Review Kubernetes Production Cluster (Full Authorization Verified)
- Monitor Slack Enterprise Grid (Full Authorization Verified)
- Examine records within Marketing Operations
- View records within Marketing Operations
- Consult records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Salesforce CRM
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: GCP Core Infrastructure, NetSuite ERP, Kubernetes Production Cluster

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Contractor (Compliance) needs to access quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to purge audit logs will trigger an immediate P0 security alert.
- Cannot tweak permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Marketing Contractor (Platform)

**Role ID:** `RL-MAR-20083`
**Department:** Marketing
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Access Jira System Admin (Full Authorization Verified)
- Audit Production Database Cluster (PostgreSQL) (Full Authorization Verified)
- View HubSpot Marketing (Full Authorization Verified)
- Access Splunk Security Logs (Full Authorization Verified)
- Read records within Marketing Operations
- Access records within Marketing Operations
- Examine records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Figma Enterprise
- Strictly forbidden from accessing GCP Core Infrastructure
- Strictly forbidden from accessing Snowflake Data Warehouse
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Jira System Admin, Production Database Cluster (PostgreSQL), HubSpot Marketing

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Contractor (Platform) needs to consult quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to remove audit logs will trigger an immediate P0 security alert.
- Cannot manage permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Geographic restriction bypass: Required for executives traveling to unrestricted zones.

---

### Marketing Contractor (Growth)

**Role ID:** `RL-MAR-20066`
**Department:** Marketing
**Reporting To:** Manager or Director
**Access Level:** 2/10
**Audit Log Level:** Standard
**Security Classification Level:** Internal Use Only

#### Permissions
- Monitor Slack Enterprise Grid (Full Authorization Verified)
- Inspect MongoDB User Data Store (Full Authorization Verified)
- View Snowflake Data Warehouse (Full Authorization Verified)
- Audit Salesforce CRM (Full Authorization Verified)
- Consult records within Marketing Operations
- Read records within Marketing Operations
- Inspect records within Marketing Operations

#### Restricted Areas
- Strictly forbidden from accessing Production Database Cluster (PostgreSQL)
- Strictly forbidden from accessing Workday HRIS
- Strictly forbidden from accessing Jira System Admin
- Cannot modify global company policies.
- Access to executive payroll systems is permanently blocked.

#### Data Access Scope
- Localized Data Scope: Limited strictly to Marketing team repositories.
- PII (Personally Identifiable Information) access is masked unless specifically requested via legal channels.

#### Systems Access
Authorized platforms: Slack Enterprise Grid, MongoDB User Data Store, Snowflake Data Warehouse

#### Escalation Rules
- Any unhandled operational block must be escalated to Manager or Director.
- High severity security incidents bypass immediate reporting and escalate to the SOC Team directly.

#### Approval Authority
- No financial approval authority.
- Code/asset deployments require peer review from Team Leads.

#### Example Use Cases
- **Scenario 1:** A Marketing Contractor (Growth) needs to review quarterly reports. They authenticate via Okta, access the dashboard, and export the masked data.

#### Denied Actions
- Attempting to terminate audit logs will trigger an immediate P0 security alert.
- Cannot update permissions of equal or higher-tier roles.

#### Cross-Department Visibility
- Completely isolated to the departmental silo to enforce least-privilege principles.

#### Exceptions & Edge Cases
- Emergency Break-Glass Access for Severity 1 Incidents.

---

