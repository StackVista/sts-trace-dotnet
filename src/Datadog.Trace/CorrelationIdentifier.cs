using System;

namespace Datadog.Trace
{
    /// <summary>
    /// An API to access the active trace and span ids.
    /// </summary>
    public static class CorrelationIdentifier
    {
        internal static readonly string ServiceNameKey = "dd.service";
        internal static readonly string ServiceVersionKey = "dd.version";
        internal static readonly string EnvKey = "dd.env";
        internal static readonly string TraceIdKey = "dd.trace_id";
        internal static readonly string SpanIdKey = "dd.span_id";

        /// <summary>
        /// Gets the trace id
        /// </summary>
        public static ulong TraceId
        {
            get
            {
                return Tracer.Instance.ActiveScope?.Span?.TraceId ?? 0;
            }
        }

        /// <summary>
        /// Gets the span id
        /// </summary>
        public static ulong SpanId
        {
            get
            {
                return Tracer.Instance.ActiveScope?.Span?.SpanId ?? 0;
            }
        }
    }
}
