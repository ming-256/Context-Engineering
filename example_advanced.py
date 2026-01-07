"""
Advanced example showing custom workflow and iterative refinement.
"""
from manus_agent import ManusAgent


def research_requirements(phase_name: str) -> str:
    """Detailed requirements research."""
    return """
### Requirements Analysis

**Functional Requirements:**
- User authentication system
- RESTful API endpoints
- Database integration
- Real-time notifications

**Non-Functional Requirements:**
- Response time < 200ms
- Support 10,000 concurrent users
- 99.9% uptime
- GDPR compliance

**Technical Constraints:**
- Must use Python 3.10+
- PostgreSQL database
- Docker deployment
- AWS infrastructure
"""


def research_technology(phase_name: str) -> str:
    """Technology stack research."""
    return """
### Technology Stack Research

**Backend Framework:**
- FastAPI (chosen for async support and performance)
- Alternative: Django (more batteries-included)
- Alternative: Flask (lighter weight)

**Database:**
- PostgreSQL (chosen for ACID compliance)
- Redis for caching and sessions

**Authentication:**
- JWT tokens
- OAuth2 integration
- Refresh token rotation

**Deployment:**
- Docker + Docker Compose
- Kubernetes for orchestration
- CI/CD via GitHub Actions
"""


def design_architecture(phase_name: str) -> str:
    """Architecture design work."""
    return """
### System Architecture

**Layered Architecture:**
1. API Layer (FastAPI routes)
2. Service Layer (business logic)
3. Data Access Layer (SQLAlchemy)
4. Database Layer (PostgreSQL)

**Design Patterns:**
- Repository pattern for data access
- Dependency injection for services
- Factory pattern for model creation
- Observer pattern for notifications

**API Design:**
```
POST /api/v1/auth/login
POST /api/v1/auth/register
GET  /api/v1/users/{id}
PUT  /api/v1/users/{id}
GET  /api/v1/notifications
```
"""


def implement_core(phase_name: str) -> str:
    """Core implementation work."""
    return """
### Implementation Status

**Completed Modules:**
- User model and database schema
- Authentication endpoints
- JWT token generation/validation
- Password hashing (bcrypt)
- Email verification flow

**Code Structure:**
```
src/
├── api/
│   ├── auth.py
│   └── users.py
├── models/
│   └── user.py
├── services/
│   ├── auth_service.py
│   └── user_service.py
└── database.py
```

**Test Coverage:** 87%
"""


def test_and_validate(phase_name: str) -> str:
    """Testing and validation work."""
    return """
### Testing Results

**Unit Tests:**
- 156 tests passed
- Coverage: 87%
- All critical paths covered

**Integration Tests:**
- API endpoint tests: PASSED
- Database integration: PASSED
- Authentication flow: PASSED

**Performance Tests:**
- Average response time: 145ms
- P95 response time: 230ms
- Concurrent users tested: 5,000

**Security Audit:**
- SQL injection: Protected (SQLAlchemy ORM)
- XSS: Protected (input sanitization)
- CSRF: Protected (token validation)
- Rate limiting: Implemented
"""


def generate_advanced_deliverable() -> str:
    """Generate comprehensive deliverable."""
    return """
## Executive Summary

Successfully implemented a production-ready web application with authentication, RESTful API, and database integration.

## Project Overview

### Objectives Achieved
- ✅ Secure user authentication system
- ✅ RESTful API with FastAPI
- ✅ PostgreSQL database integration
- ✅ Real-time notification system
- ✅ Comprehensive test coverage (87%)
- ✅ Performance targets met (145ms avg response)

### Technology Stack
- **Backend:** FastAPI 0.104.1
- **Database:** PostgreSQL 15
- **Cache:** Redis 7
- **Authentication:** JWT + OAuth2
- **Deployment:** Docker + Kubernetes

## Architecture

### System Design
The application follows a layered architecture pattern with clear separation of concerns:

1. **API Layer:** FastAPI routes and endpoint handlers
2. **Service Layer:** Business logic and orchestration
3. **Data Access Layer:** SQLAlchemy ORM repositories
4. **Database Layer:** PostgreSQL with Redis caching

### Key Components

#### Authentication System
- JWT-based authentication with refresh tokens
- OAuth2 integration (Google, GitHub)
- Email verification workflow
- Password reset functionality
- Secure password hashing (bcrypt)

#### API Endpoints
- User registration and authentication
- Profile management (CRUD operations)
- Notification system
- Admin endpoints
- Health check and metrics

#### Database Schema
- Users table with encrypted credentials
- Sessions table for active tokens
- Notifications table for messages
- Audit log for security events

## Implementation Highlights

### Security Features
- Input validation and sanitization
- SQL injection protection (ORM)
- XSS protection
- CSRF token validation
- Rate limiting (100 req/min per IP)
- Secure session management
- HTTPS enforcement

### Performance Optimizations
- Redis caching for frequent queries
- Database query optimization
- Async request handling
- Connection pooling
- Static asset CDN integration

### Code Quality
- Type hints throughout codebase
- Comprehensive docstrings
- PEP 8 compliance
- 87% test coverage
- Code review guidelines followed

## Testing

### Test Results
- **Unit Tests:** 156/156 passed
- **Integration Tests:** 24/24 passed
- **E2E Tests:** 12/12 passed
- **Performance Tests:** All targets met
- **Security Audit:** No critical issues

### Performance Metrics
- Average Response Time: 145ms
- P95 Response Time: 230ms
- P99 Response Time: 420ms
- Throughput: 2,500 req/sec
- Error Rate: 0.02%

## Deployment

### Infrastructure
- Docker containers for all services
- Kubernetes for orchestration
- AWS EKS for managed Kubernetes
- RDS for PostgreSQL
- ElastiCache for Redis

### CI/CD Pipeline
- Automated testing on PR
- Docker image building
- Security scanning
- Automated deployment to staging
- Manual approval for production

### Monitoring
- Prometheus for metrics
- Grafana dashboards
- ELK stack for logging
- Sentry for error tracking
- Uptime monitoring

## Documentation

### Available Documentation
- API documentation (OpenAPI/Swagger)
- Architecture decision records (ADRs)
- Deployment runbook
- Developer setup guide
- API integration guide
- Security best practices

## Future Enhancements

### Phase 2 Features (Q2 2026)
- Multi-factor authentication (MFA)
- Advanced role-based access control (RBAC)
- Webhook system for integrations
- GraphQL API endpoint
- Mobile app support

### Phase 3 Features (Q3 2026)
- Microservices architecture migration
- Event-driven architecture
- Machine learning recommendations
- Real-time collaboration features
- Advanced analytics dashboard

## Conclusion

The project successfully delivered a production-ready web application that meets all functional and non-functional requirements. The system demonstrates:

- **Robust Security:** Multiple layers of security protection
- **High Performance:** Meets all performance targets
- **Scalability:** Can handle 10,000+ concurrent users
- **Maintainability:** Clean code with 87% test coverage
- **Reliability:** 99.9% uptime target achievable

The foundation is solid for future enhancements and scale.

## Appendices

### A. API Endpoints Summary
See full API documentation at: `/docs` (Swagger UI)

### B. Database Schema
See schema diagram in: `docs/database-schema.png`

### C. Performance Test Results
See detailed metrics in: `docs/performance-report.pdf`

### D. Security Audit Report
See full report in: `docs/security-audit.pdf`
"""


def main():
    """Advanced example with detailed phases."""
    print("\n" + "="*70)
    print("Advanced Manus Agent Example - Web Application Development")
    print("="*70 + "\n")
    
    # Create agent
    agent = ManusAgent(output_dir="output")
    
    # Define detailed task
    task = "Build a production-ready web application with authentication"
    
    # Define specific phases
    phases = [
        "Gather and analyze requirements",
        "Research technology stack and tools",
        "Design system architecture",
        "Implement core functionality",
        "Test and validate the system",
        "Prepare production deployment"
    ]
    
    # Start the task
    agent.start_task(task, phases)
    
    # Manual phase execution with detailed callbacks
    print("Phase 1: Requirements Analysis")
    agent.execute_phase(0, research_callback=research_requirements)
    agent.print_status()
    
    print("\nPhase 2: Technology Research")
    agent.execute_phase(1, research_callback=research_technology)
    agent.print_status()
    
    print("\nPhase 3: Architecture Design")
    agent.execute_phase(2, work_callback=design_architecture)
    agent.print_status()
    
    print("\nPhase 4: Implementation")
    agent.execute_phase(3, work_callback=implement_core)
    agent.print_status()
    
    print("\nPhase 5: Testing & Validation")
    agent.execute_phase(4, work_callback=test_and_validate)
    agent.print_status()
    
    print("\nPhase 6: Deployment Preparation")
    agent.execute_phase(5)
    agent.print_status()
    
    # Generate comprehensive deliverable
    print("\nGenerating Final Deliverable...")
    agent.generate_deliverable(
        title="Web Application Development - Final Report",
        content_generator=generate_advanced_deliverable
    )
    
    # Final status
    print("\n" + "="*70)
    print("PROJECT COMPLETED!")
    print("="*70)
    agent.print_status()
    
    print("\nDeliverables Available:")
    print("  📋 plan.md - Complete project plan with all phases tracked")
    print("  📝 notes.md - Detailed research and implementation notes")
    print("  📄 deliverable.md - Comprehensive final report")
    print("\nLocation: ./output/")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
