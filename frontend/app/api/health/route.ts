import { NextResponse } from "next/server"

export async function GET() {
  try {
    // Check if the CrewAI backend is accessible
    const backendUrl = process.env.CREWAI_BACKEND_URL || "http://localhost:12000"
    
    let backendStatus = "unknown"
    try {
      const response = await fetch(`${backendUrl}/health`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        },
        // Add timeout
        signal: AbortSignal.timeout(5000)
      })
      
      if (response.ok) {
        backendStatus = "healthy"
      } else {
        backendStatus = "unhealthy"
      }
    } catch (error) {
      backendStatus = "unreachable"
    }

    return NextResponse.json({
      status: "healthy",
      timestamp: new Date().toISOString(),
      service: "TradieMate Marketing Analytics Frontend",
      version: "1.0.0",
      backend: {
        url: backendUrl,
        status: backendStatus
      },
      environment: process.env.NODE_ENV || "development"
    })
  } catch (error) {
    return NextResponse.json(
      {
        status: "unhealthy",
        timestamp: new Date().toISOString(),
        error: error instanceof Error ? error.message : "Unknown error"
      },
      { status: 500 }
    )
  }
}