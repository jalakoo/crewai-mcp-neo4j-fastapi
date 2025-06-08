import { NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  try {
    const { messages } = await request.json()
    
    // Get the latest user message
    const userMessage = messages[messages.length - 1]?.content || ""
    
    // Get the CrewAI FastAPI backend URL from environment
    const backendUrl = process.env.CREWAI_BACKEND_URL || "http://localhost:12000"
    
    // Call our CrewAI FastAPI backend
    const response = await fetch(`${backendUrl}/crewai`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // Forward any API key if provided
        ...(process.env.CREWAI_API_KEY && {
          "X-API-Key": process.env.CREWAI_API_KEY
        })
      },
      body: JSON.stringify({
        query: userMessage
      })
    })

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}))
      throw new Error(`CrewAI backend error: ${response.status} - ${errorData.detail || response.statusText}`)
    }

    const result = await response.json()
    
    // Format the response for the chat interface
    const formattedResponse = formatCrewAIResponse(result)
    
    // Return a streaming response compatible with the chat interface
    const stream = new ReadableStream({
      start(controller) {
        const encoder = new TextEncoder()
        
        // Send the formatted response as a stream
        const chunk = encoder.encode(`data: ${JSON.stringify({
          choices: [{
            delta: {
              content: formattedResponse
            }
          }]
        })}\n\n`)
        
        controller.enqueue(chunk)
        
        // Send the final chunk
        const finalChunk = encoder.encode(`data: [DONE]\n\n`)
        controller.enqueue(finalChunk)
        controller.close()
      }
    })

    return new Response(stream, {
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
      }
    })

  } catch (error) {
    console.error("CrewAI API Error:", error)
    
    return NextResponse.json(
      { 
        error: "Failed to process marketing analytics query",
        detail: error instanceof Error ? error.message : "Unknown error"
      },
      { status: 500 }
    )
  }
}

function formatCrewAIResponse(result: any): string {
  // Format the CrewAI response for better display in the chat interface
  let formattedResponse = ""
  
  if (result.status === "success" || result.status === "completed") {
    formattedResponse += "# 📊 Marketing Analytics Report\n\n"
    
    // Add the main result
    if (result.result) {
      formattedResponse += result.result + "\n\n"
    }
    
    // Add any additional insights
    if (result.insights) {
      formattedResponse += "## 💡 Key Insights\n\n"
      if (Array.isArray(result.insights)) {
        result.insights.forEach((insight: string, index: number) => {
          formattedResponse += `${index + 1}. ${insight}\n`
        })
      } else {
        formattedResponse += result.insights + "\n"
      }
      formattedResponse += "\n"
    }
    
    // Add recommendations
    if (result.recommendations) {
      formattedResponse += "## 🎯 Recommendations\n\n"
      if (Array.isArray(result.recommendations)) {
        result.recommendations.forEach((rec: string, index: number) => {
          formattedResponse += `${index + 1}. ${rec}\n`
        })
      } else {
        formattedResponse += result.recommendations + "\n"
      }
      formattedResponse += "\n"
    }
    
    // Add performance metrics if available
    if (result.metrics) {
      formattedResponse += "## 📈 Performance Metrics\n\n"
      if (typeof result.metrics === "object") {
        Object.entries(result.metrics).forEach(([key, value]) => {
          formattedResponse += `- **${key}**: ${value}\n`
        })
      } else {
        formattedResponse += result.metrics + "\n"
      }
      formattedResponse += "\n"
    }
    
    // Add agent information
    if (result.agent_used) {
      formattedResponse += `---\n*Analysis performed by: ${result.agent_used}*\n`
    }
    
  } else {
    // Handle error cases
    formattedResponse = "❌ **Error Processing Marketing Query**\n\n"
    formattedResponse += result.error || result.detail || "An unexpected error occurred while analyzing your marketing data."
    
    if (result.suggestions) {
      formattedResponse += "\n\n**Suggestions:**\n"
      formattedResponse += result.suggestions
    }
  }
  
  return formattedResponse
}